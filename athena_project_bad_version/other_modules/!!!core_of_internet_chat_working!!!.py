import pymysql
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout

connection = pymysql.connect("185.224.138.49", "u799736401_for_Athena", "0MechTa8", "u799736401_for_Athena", charset="utf8")
cursor = connection.cursor()
cursor.execute("SELECT * FROM messages")
row = cursor.fetchone()
connection.close()
print(str(row[0]) + "|" + str(row[1]) + "|" + str(row[3]) + "|")


class MainPartOfChatModule(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_part_of_chat_module = OtherPartsOfChatModule(parent=self)
        self.setCentralWidget(self.main_part_of_chat_module)


class OtherPartsOfChatModule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        test_label = QLabel("Hello", self)
        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(test_label)
        self.setLayout(vbox_1)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfChatModule()
    program.show()
    sys.exit(application.exec_())
