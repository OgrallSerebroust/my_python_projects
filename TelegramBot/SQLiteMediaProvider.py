from SQLiteSettings import cursor, database


async def save_media_data(url: str, file_id: str):
    media_img_data = (url, file_id)
    cursor.execute("INSERT INTO media_img_urls_storage (url, file_id) VALUES (?, ?)", media_img_data)
    database.commit()


async def take_media_img_data(last_img_id):
    media_img_data = cursor.execute(
        "SELECT url, file_id FROM media_img_urls_storage WHERE media_img_id == '{last_img_id}'".format(
            last_img_id=last_img_id)).fetchone()
    database.commit()
    return media_img_data
