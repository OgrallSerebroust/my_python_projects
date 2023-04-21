import sqlite3

database = sqlite3.connect("MainMediaDataStorage.db")
database.row_factory = sqlite3.Row  # Для [], а не () на выходе
cursor = database.cursor()


async def start_database():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS media_img_urls_storage(media_img_id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT, file_id TEXT)")
    database.commit()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS global_bot_settings(setting_id INTEGER PRIMARY KEY AUTOINCREMENT, variable_name TEXT, variable_value TEXT, variable_type TEXT)")
    database.commit()
