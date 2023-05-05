from SQLiteSettings import database, cursor


def take_bot_token_const():
    return cursor.execute("SELECT * FROM global_bot_settings WHERE variable_name == 'bot_token'").fetchone()


async def set_last_img_id_data():
    cursor.execute("INSERT INTO global_bot_settings (variable_name, variable_value, variable_type) VALUES (?, ?, ?)",
                   ("last_img_id", "1", "int"))
    database.commit()


async def take_last_img_id_data():
    last_img_data = cursor.execute(
        "SELECT variable_value, variable_type FROM global_bot_settings WHERE variable_name == 'last_img_id'").fetchone()
    database.commit()
    return last_img_data


async def save_last_img_id_data(last_img_id):
    cursor.execute(
        "UPDATE global_bot_settings SET variable_value = '{last_img_id}' WHERE variable_name == 'last_img_id'".format(
            last_img_id=last_img_id))
    database.commit()
