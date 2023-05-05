import datetime
import logging
import os
import random
from aiogram import Bot, Dispatcher, executor, types, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from SQLiteSettings import start_database
from SQLiteMediaProvider import save_media_data, take_media_img_data
from SQLiteSettingsProvider import take_bot_token_const, set_last_img_id_data, take_last_img_id_data, save_last_img_id_data

bot = Bot(token=take_bot_token_const()["variable_value"])
dp = Dispatcher(bot)
# jobstores = {
#     'mongo': MongoDBJobStore(),
#     'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
# }
# executors = {
#     'default': ThreadPoolExecutor(20),
#     'processpool': ProcessPoolExecutor(5)
# }
job_defaults = {
    #'coalesce': False,
    "max_instances": 1
}
scheduler = AsyncIOScheduler(job_defaults=job_defaults, timezone="Europe/Moscow")
last_img_id = 0
send_photos_job_id = ""
logging.basicConfig(level=logging.INFO)


async def type_media(chat_id):
    global last_img_id
    media = types.MediaGroup()
    current_media_path = await take_media_img_data(last_img_id=last_img_id)
    if current_media_path:
        media.attach_photo(types.InputFile(os.getcwd() + current_media_path["url"]))
        await types.ChatActions.upload_photo()
        await bot.send_media_group(media=media, chat_id=chat_id)
        last_img_id = int(last_img_id) + 1
        await save_last_img_id_data(last_img_id)
    else:
        await bot.send_message(chat_id=chat_id, text="Увы у меня закончились фоточки...")


@dp.message_handler(filters.CommandStart())
async def type_welcome(message: types.Message):
    await message.reply("Привет! Я телеграм версия Афины, пока мои функции очень ограничены, но я буду стараться становиться лучше!")  # TODO Приглашение
    await bot.send_message(chat_id=message.chat.id, text="Я обновилась! Вы так долго ждали и наконец-то я теперь умею воспринимать и записывать более одного фото в одном сообщении. Так что можете смело отправлять мне их группами. Всё будет записано и доставлено к нам в беседу.\n\nВ настоящий момент моя версия 1.0.1\n\nПовестка запланированного обновления: Вернуться к предыдущей версии с пакетами, попробовать повторить разделение проекта, но на этот раз с роутерами. Включить первые мидлвари, для создания статуса состояния. Если коротко, готовимся подключению первых моделей.")
    
    await bot.send_sticker(chat_id=message.chat.id, sticker=r"CAACAgIAAxkBAAEI3ZJkVRIRKzucVmEtXW4N3Ozf4XDslQACEA8AAtshKUpHGRKDuupttS8E")
    #message.from_user.id


@dp.message_handler(filters.Command("startSendingPhotos"))
async def start_schedule_send_photos(message: types.Message):
    global send_photos_job_id
    chat_id = message.chat.id
    if not scheduler.get_jobs():
        await message.reply("Ура! Вы пришли за новой порцией фоточек!")
        job = scheduler.add_job(type_media, "interval", hours=1, args=(chat_id,), id="1")
        send_photos_job_id = job.id
    else:
        for _ in scheduler.get_jobs():
            if not _.id == send_photos_job_id:
                await message.reply("Ура! Вы пришли за новой порцией фоточек!")
                job = scheduler.add_job(type_media, "interval", hours=1, args=(chat_id,), id="1")
                send_photos_job_id = job.id
            else:
                await message.reply("Простите, но я уже и так иногда отсылаю вам фоточки... Может вы перепутали что-то?")


@dp.message_handler(filters.Command("stopSendingPhotos"))
async def stop_schedule_send_photos(message: types.Message):
    for _ in scheduler.get_jobs():
        if _.name == "type_media":
            scheduler.remove_job(_.id)
            await message.reply(text="Так и быть, я перестаю отправлять фотографии о которых вы просили")


@dp.message_handler(content_types='photo')
async def save_users_img(message: types.Message):
    media_img_file_path = "/media/" + datetime.datetime.now().strftime(
        "%Y%m%d") + "/" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random.random()) + ".jpg"
    photos = message.photo[-1]
    await photos.download(destination_file=os.getcwd() + media_img_file_path)
    await save_media_data(url=media_img_file_path, file_id=photos.file_id)


# @dp.message_handler()
# async def echo(message: types.Message):
   # await message.answer(message.text)


async def on_startup(_):
    await start_database()
    last_img_data = await take_last_img_id_data()
    if not last_img_data:
        await set_last_img_id_data()
        global last_img_id
        last_img_id = 1
    else:
        last_img_id = last_img_data["variable_value"]


async def on_shutdown(_):
    await save_last_img_id_data(last_img_id)


if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
