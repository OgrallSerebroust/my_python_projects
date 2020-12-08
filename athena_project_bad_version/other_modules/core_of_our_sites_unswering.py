import sys
import pymysql
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class MainPartOfOurApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_part_of_our_app_in_widget = OtherPartsOfOurApp(parent=self)
        self.setCentralWidget(self.main_part_of_our_app_in_widget)
        self.setWindowTitle("Core of chat communication")


class OtherPartsOfOurApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        label_for_new_messages = QLabel("New messages in database", self)
        label_for_answers = QLabel("Completed answers on messages", self)
        self.table_for_new_messages = pg.TableWidget()
        self.table_for_new_messages.setData("good")
        button_for_starting_work = QPushButton("Starting confirmed", self)
        button_for_starting_work.clicked.connect(self.start_messaging)
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(label_for_new_messages)
        hbox_1.addWidget(label_for_answers)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        vbox_1.addWidget(self.table_for_new_messages)
        vbox_1.addWidget(button_for_starting_work)
        self.setLayout(vbox_1)

    def start_messaging(self):
        connection = pymysql.connect("185.224.138.49", "u799736401_for_Athena", "0MechTa8", "u799736401_for_Athena",
                                     charset="utf8")
        local_connection = pymysql.connect("127.0.0.1", "athena", "0MechTa8", "first_ini_db_for_athena", charset="utf8")
        cursor = connection.cursor()
        local_cursor = local_connection.cursor()
        local_cursor.execute(
            "SELECT * FROM first_ini_local_table_for_athena WHERE name_of_setting='date_and_time_of_last_db_check'")
        local_row = local_cursor.fetchone()
        date_and_time_of_last_checking_message = local_row[2]
        local_connection.close()
        query = "SELECT * FROM messages WHERE date>'" + str(date_and_time_of_last_checking_message) + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        self.table_for_new_messages.setData(rows)
        with open("temp_data_from_chat.yml", "w") as temp_data_file:
            for row in rows:
                temp_data_file.write("- " + str(row[1]) + "\n")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfOurApp()
    program.show()
    sys.exit(application.exec_())
