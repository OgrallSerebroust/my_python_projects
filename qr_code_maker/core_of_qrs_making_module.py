import sys
import pyqrcode
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor, QPixmap, QFont, QFontDatabase
from PyQt5.QtCore import Qt


class MainPartOfQrsMakingModule(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        stylesheet = """
        .QLabel
        {
            background: rgba(1, 72, 126, 0.8);
            color: #54A8CC;
            border: 2px solid #01487E;
            padding: 2px 3px;
        }
        
        .QLineEdit
        {
            background: rgba(1, 72, 126, 0.8);
            color: #54A8CC;
            border: 2px solid #01487E;
            padding: 2px 3px;
        }
        
        .QPushButton
        {
            background: rgba(1, 72, 126, 0.8);
            border:2px solid #01487E;
            color: #54A8CC;
            padding: 3px 3px;
        }
        
        .QPushButton:hover
        {
            background: rgba(1, 32, 76, 0.5);
        }
        """
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))
        fot_id = QFontDatabase.addApplicationFont("../media/oformlenie/fonts/Oxanium-Medium.ttf")
        font_str = QFontDatabase.applicationFontFamilies(fot_id)[0]
        font = QFont(font_str, 14)
        self.main_part_of_qrs_making_module = OtherPartsOfQrsMakingModule(parent=self)
        self.setCentralWidget(self.main_part_of_qrs_making_module)
        self.setPalette(palette)
        self.setFont(QFont(font))
        self.setWindowTitle("QR coder")
        self.setStyleSheet(stylesheet)


class OtherPartsOfQrsMakingModule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        label_for_importing_text_for_qr = QLabel("Please, enter the key: ", self)
        self.editline_for_importing_text_for_qr = QLineEdit()
        button_for_importing_text_for_qr = QPushButton("Generate")
        button_for_importing_text_for_qr.clicked.connect(self.generate_our_qr_code)
        label_about_picture = QLabel("That's your QR code: ", self)
        label_about_picture.setAlignment(Qt.AlignCenter)
        self.label_for_picture_with_qr = QLabel(self)
        self.label_for_picture_with_qr.setStyleSheet("""
        min-width:290px;
        min-height:290px;
        padding: 0;
        background:#FFFFFF;
        """)
        self.label_for_picture_with_qr.setAlignment(Qt.AlignCenter)
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(label_for_importing_text_for_qr)
        hbox_1.addWidget(self.editline_for_importing_text_for_qr)
        hbox_1.addWidget(button_for_importing_text_for_qr)
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(label_about_picture)
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.label_for_picture_with_qr)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        vbox_1.addLayout(hbox_2)
        vbox_1.addLayout(hbox_3)
        self.setLayout(vbox_1)

    def generate_our_qr_code(self):
        text_for_qr_code = self.editline_for_importing_text_for_qr.text()
        if text_for_qr_code != '':
            generated_qr_code = pyqrcode.create(text_for_qr_code)
            url_to_place_with_generated_qr_code = "../media/qr_codes/"
            name_of_generated_qr_code = url_to_place_with_generated_qr_code + text_for_qr_code + ".png"
            generated_qr_code.png(name_of_generated_qr_code, scale=10)
            pixmap = QPixmap(name_of_generated_qr_code)
            self.label_for_picture_with_qr.setPixmap(pixmap)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfQrsMakingModule()
    program.show()
    sys.exit(application.exec_())
