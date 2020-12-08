import sys
import pymysql
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor, QFont

connection = pymysql.connect("185.224.138.49", "u799736401_for_Athena", "0MechTa8", "u799736401_for_Athena", charset="utf8")
cursor = connection.cursor()
cursor.execute("SELECT * FROM passwords_memory")
rows = cursor.fetchall()
connection.close()


class MainPartOfPasswordWorkingModule(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        stylesheet = """
        .QLabel
        {
            background: rgba(204, 68, 0, 0.8);
            color: #FFAF87;
            border: 2px solid #FF5500;
            padding: 2px 3px;
        }
        
        .QLineEdit
        {
            background: rgba(204, 68, 0, 0.8);
            color: #FFAF87;
            border: 2px solid #FF5500;
            padding: 2px 3px;
        }
        
        .QPushButton
        {
            background: rgba(204, 68, 0, 0.8);
            color: #FFAF87;
            border: 2px solid #FF5500;
            padding: 2px 3px;
        }
        
        .QPushButton:hover
        {
            background: rgba(128, 42, 0, 0.8);
        }
        """
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))
        self.main_part_of_password_working_module = OtherPartsOfPasswordWorkingModule(parent=self)
        self.setCentralWidget(self.main_part_of_password_working_module)
        self.setPalette(palette)
        self.setFont(QFont("Oxanium-Medium", 14))
        self.setWindowTitle("Known passwords")
        self.setStyleSheet(stylesheet)


class OtherPartsOfPasswordWorkingModule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.table_with_passwords = pg.TableWidget()
        self.table_with_passwords.setData(rows)
        self.table_with_passwords.setStyleSheet("""
        .TableWidget
        {
            background: #000000;
            color: #FFAF87;
        }
        """)
        self.table_with_passwords.horizontalHeader().hide()
        self.table_with_passwords.verticalHeader().hide()
        label_about_deleting = QLabel("If you want delete one of passwords, please enter id number of this, below...", self)
        self.editline_for_number_of_password_for_deleting = QLineEdit()
        button_for_confirm_deleting = QPushButton("DELETE")
        button_for_confirm_deleting.clicked.connect(self.delete_password)
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.table_with_passwords)
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(label_about_deleting)
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.editline_for_number_of_password_for_deleting)
        hbox_3.addWidget(button_for_confirm_deleting)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        vbox_1.addLayout(hbox_2)
        vbox_1.addLayout(hbox_3)
        self.setLayout(vbox_1)

    def delete_password(self):
        number_of_password_for_deleting = self.editline_for_number_of_password_for_deleting.text()
        connection_for_deleting = pymysql.connect("185.224.138.49", "u799736401_for_Athena", "0MechTa8", "u799736401_for_Athena", charset="utf8")
        cursor_for_deleting = connection_for_deleting.cursor()
        cursor_for_deleting.execute("DELETE FROM passwords_memory WHERE id=%s", number_of_password_for_deleting)
        connection_for_deleting.commit()
        connection_for_deleting.close()
        connection_for_updating_table = pymysql.connect("185.224.138.49", "u799736401_for_Athena", "0MechTa8", "u799736401_for_Athena", charset="utf8")
        cursor_for_updating_table = connection_for_updating_table.cursor()
        cursor_for_updating_table.execute("SELECT * FROM passwords_memory")
        new_rows = cursor_for_updating_table.fetchall()
        connection_for_updating_table.close()
        self.table_with_passwords.setData(new_rows)
        self.editline_for_number_of_password_for_deleting.setText("")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfPasswordWorkingModule()
    program.show()
    sys.exit(application.exec_())
