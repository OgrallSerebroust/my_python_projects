from SQLiteSettings import database, cursor


def take_bot_token_const():
    return cursor.execute("SELECT * FROM global_bot_settings WHERE variable_name == 'bot_token'").fetchone()


async def set_last_img_id_data():
    cursor.execute("INSERT INTO global_bot_settings (variable_name, variable_value, variable_type) VALUES (?, ?, ?)",
                   ("last_img_id", "1", "int"))
    database.commit()
