import sys
import youtube_dl
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon

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
        button_of_destination_browsing.clicked.connect(self.Browse_of_destination)
        button_of_confirming_downloading = QPushButton("Download video")
        button_of_confirming_downloading.clicked.connect(self.Confirm_downloading)
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
        self.setWindowTitle("YouTube video downloader")
        self.setWindowIcon(QIcon("media/img/window_icon_V1.png"))

    def Browse_of_destination(self):
        name_of_destination = QFileDialog.getExistingDirectory(None, "Select the destination", "\home")
        self.our_destination.setText(name_of_destination)
    
    def Confirm_downloading(self):
        our_youtube_link, our_completed_destination, our_temp_destination = self.our_link.text(), self.our_destination.text(), "media/video/"
        if(our_youtube_link):
            Location = '%s \%(extractor)s-%(id)s-%(title)s.%(ext)s'.replace("%s ", our_temp_destination)
            ytdl_format_options = {'outtmpl': Location, "format": "bestvideo + bestaudio"}
            with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
                ydl.download([our_youtube_link])
                self.Complete_downloading(our_completed_destination)

    def Complete_downloading(self, our_completed_destination):
        os.chdir("media/video/")
        video = VideoFileClip(os.listdir()[1])
        audio = AudioFileClip(os.listdir()[0])
        new_video = video.set_audio(audio)
        new_video.write_videofile(our_completed_destination + "/completed.mp4")
        os.remove(os.listdir()[1])
        os.remove(os.listdir()[0])
        print("OK!")
        
if __name__ == "__main__":
    our_gui_application = QApplication(sys.argv)
    program = Our_gui()
    program.show()
    sys.exit(our_gui_application.exec_())