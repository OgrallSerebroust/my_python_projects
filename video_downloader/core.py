import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

class Our_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label_what_link = QLabel("Please, enter the link of YouTube video: ", self)
        self.our_link = QLineEdit()
        label_of_destination = QLabel("Please, choose the destination of our video...", self)
        self.our_destination = QLineEdit()
        button_of_destination_browsing = QPushButton("Browse", self)
        #button_of_destination_browsing.clicked.connect() #!----------
        button_of_confirming_downloading = QPushButton("Download video")
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(label_what_link)
        hbox_1.addWidget(self.our_link)
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(label_of_destination)
        hbox_2.addWidget(self.our_destination)
        hbox_2.addWidget(button_of_destination_browsing)
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(button_of_confirming_downloading)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        self.setLayout(vbox)
        
if __name__ == "__main__":
    our_gui_application = QApplication(sys.argv)
    program = Our_gui()
    program.show()
    sys.exit(our_gui_application.exec_())