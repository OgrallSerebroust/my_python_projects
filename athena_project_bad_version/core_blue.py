import sys
import random
import os
import playsound
import pickle
import speech_recognition as sr
import numpy as np
import datetime
import subprocess
from gtts import gTTS
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QWidget, QLabel, QPushButton, QLineEdit, \
    QPlainTextEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont, QFontDatabase, QPixmap
from PyQt5.QtCore import Qt, QSize
from tensorflow.keras.models import load_model
from tensorflow.keras import preprocessing
from dataclasses import dataclass
import core_of_passwords_maker


@dataclass
class MessageFromUser:
    id: int
    text: str
    user: str


master_mode = True
voice_is_on = True
one_good_message_info = MessageFromUser
active_chat_module, active_passwords_module = False, False


class MainPartOfOurApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        stylesheet = """
        .QPushButton
        {
            background: rgba(1, 72, 126, 0.8);
            border:2px solid #01487E;
            height: 50px;
            color: #54A8CC;
            border-radius: 13px;
        }
        
        .QPushButton:hover
        {
            background: rgba(1, 32, 76, 0.5);
        }
        
        .QPushButton:focus
        {
            background: rgba(1, 32, 76, 0.8);
        }
        
        .QLabel
        {
            background: rgba(1, 72, 126, 0.8);
            color: #54A8CC;
            border: 2px solid #01487E;
            min-width: 456px;
        }
        
        .QLineEdit
        {
            background: rgba(1, 72, 126, 0.8);
            color: #54A8CC;
            border: 2px solid #01487E;
            height: 350px;
            border-radius: 13px;
            padding:2px 3px;
        }
        
        QPlainTextEdit
        {
            background: rgba(1, 72, 126, 0.8);
            color: #54A8CC;
            border: 2px solid #01487E;
            min-width: 456px;
            border-radius: 13px;
        }
        """
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            background: rgba(1, 32, 76, 0.5);
            color: #54A8CC;
        """)
        file_menu = menubar.addMenu("File")
        close_action = QAction("Exit", self)
        file_menu.addAction(close_action)
        close_action.triggered.connect(qApp.exit)
        environment_menu = menubar.addMenu("Environment")
        internet_chat_working_action = QAction("Internet chat working", self)
        if master_mode:
            passwords_working_module = QAction("Work with passwords", self)
            environment_menu.addAction(passwords_working_module)
            passwords_working_module.triggered.connect(self.open_window_of_password_working)
        environment_menu.addAction(internet_chat_working_action)
        internet_chat_working_action.triggered.connect(self.open_window_of_internet_chat)
        tools_menu = menubar.addMenu("Tools")
        qr_making_module = QAction("Made QR-code", self)
        tools_menu.addAction(qr_making_module)
        qr_making_module.triggered.connect(self.open_qr_code_making_module)
        about_menu = menubar.addMenu("About")
        map_of_network_brain = QAction("Map of Athena's brains", self)
        about_menu.addAction(map_of_network_brain)
        map_of_network_brain.triggered.connect(self.show_map_of_networks_brain)
        self.main_part_of_our_app_in_widget = OtherPartsOfOurApp(parent=self)
        self.setCentralWidget(self.main_part_of_our_app_in_widget)
        background_image = QImage("media/oformlenie/img/Background_2V.jpg")
        scaled_background_image = background_image.scaled(QSize(1920, 1100))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_background_image))
        fot_id = QFontDatabase.addApplicationFont("media/oformlenie/fonts/Oxanium-Medium.ttf")
        font_str = QFontDatabase.applicationFontFamilies(fot_id)[0]
        font = QFont(font_str, 14)
        self.showMaximized()
        self.setPalette(palette)
        self.showFullScreen()
        self.setWindowTitle("Athena project")
        self.setFont(QFont(font))
        self.setStyleSheet(stylesheet)

    # Нижеследующие 2 функции предельно опасны, недоработаны и являются отключенными

    @staticmethod
    def clearing_our_data_from_message(all_data):
        finding_number_of_message, finding_text, finding_user = True, False, False
        good_text_from_message, good_number_of_message, good_user_from_message = '', '', ''
        for sign in all_data:
            if finding_number_of_message and sign != "|":
                good_number_of_message += sign
            elif finding_number_of_message and sign == "|":
                finding_number_of_message, finding_text = finding_text, finding_number_of_message
            elif finding_text and sign != "|":
                good_text_from_message += sign
            elif finding_text and sign == "|":
                finding_text, finding_user = finding_user, finding_text
            elif finding_user and sign != "|":
                good_user_from_message += sign
        one_good_message_info.id, one_good_message_info.text, one_good_message_info.user = good_number_of_message, good_text_from_message, good_user_from_message

    def start_internet_chat_working(self):
        global active_chat_module
        active_chat_module = True
        core_url_for_internet_chat_working = "D:/Python3_6_8/my_projects/Athena_project/Version_1.0_pre_alfa" \
                                             "/other_modules/core_of_internet_chat_working.py"
        process = subprocess.Popen(core_url_for_internet_chat_working, stdout=subprocess.PIPE, shell=True)
        text, _ = process.communicate()
        our_good_data_from_one_message = str(text)[2:][:-5]
        self.clearing_our_data_from_message(our_good_data_from_one_message)

    def open_window_of_internet_chat(self):
        global active_chat_module
        core_url_for_internet_chat_working = "D:/Python3_6_8/my_projects/Athena_project/Version_1.0_pre_alfa" \
                                             "/other_modules/core_of_our_sites_unswering.py"
        process = subprocess.Popen(core_url_for_internet_chat_working, stdout=subprocess.PIPE, shell=True)
        active_chat_module = True

    def open_window_of_password_working(self):
        global active_passwords_module
        if master_mode:
            core_of_password_working = "D:/Python3_6_8/my_projects/Athena_project/Version_1.0_pre_alfa" \
                                             "/other_modules/core_of_password_working.py"
            process = subprocess.Popen(core_of_password_working, stdout=subprocess.PIPE, shell=True)
            active_passwords_module = True
        else:
            print("Access denied!")

    def open_qr_code_making_module(self):
        core_of_qrs_making_module = "D:/Python3_6_8/my_projects/Athena_project/Version_1.0_pre_alfa" \
                                             "/other_modules/core_of_qrs_making_module.py"
        process = subprocess.Popen(core_of_qrs_making_module, stdout=subprocess.PIPE, shell=True)
        text, _ = process.communicate()

    def show_map_of_networks_brain(self):
        core_url_for_map_of_networks_brain = "D:/Python3_6_8/my_projects/Athena_project/Version_1.0_pre_alfa" \
                                             "/other_modules/core_of_brain_places_visualisation.py"
        process = subprocess.Popen(core_url_for_map_of_networks_brain, stdout=subprocess.PIPE, shell=True)
        #text, _ = process.communicate()


class OtherPartsOfOurApp(QWidget):
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    model = load_model("model.h5")
    model.summary()
    enc_model = load_model("encoder_model.h5")
    enc_model.summary()
    dec_model = load_model("decoder_model.h5")
    dec_model.summary()
    maxlen_questions = 22
    maxlen_answers = 74

    def __init__(self, parent=None):
        super().__init__(parent)
        print("Объявление и инициализация необходимых переменных...")
        self.is_it_first_task = True
        self.date_and_time_of_start = str(datetime.datetime.now())
        print("Инициализация завершена")
        project = QLabel("Project Athena", self)
        project.setAlignment(Qt.AlignCenter)
        project.setStyleSheet("""
            background: none;
            border: none;
            font-size: 35pt;
            font-weight: bold;
        """)
        avatar = QLabel(self)
        avatar.setStyleSheet("""
            width: 456px;
            height: 456px;
        """)
        our_avatar_image = QPixmap("media/oformlenie/img/Athena_1.png")
        scaled_our_avatar_image = our_avatar_image.scaled(QSize(456, 456))
        avatar.setPixmap(scaled_our_avatar_image)
        self.voice_trigger = QPushButton("Voice is ON", self)
        self.voice_trigger.clicked.connect(self.voice_triggering)
        self.start_checking_of_our_chat_on_our_site_button = QPushButton("Start Chat Checking", self)
        self.start_checking_of_our_chat_on_our_site_button.clicked.connect(self.start_checking_of_our_chat_on_our_site)
        self.status = QPlainTextEdit(self)
        self.status.setReadOnly(True)
        self.status.setStyleSheet("""
            border-radius: 0;
            font-size: 10pt;
        """)
        self.status.appendPlainText("Data and time of execution: " + str(self.date_and_time_of_start))
        self.status.appendPlainText("Data and time of the last status update: " + str(datetime.datetime.now()))
        self.status.appendPlainText("Voice answering: " + str(self.voice_trigger.text()[9:]))
        self.status.appendPlainText("You are master: " + str(master_mode))
        self.status.appendPlainText("Internet chat module: " + str(active_chat_module))
        self.status.appendPlainText("Data and time of the last database check: " + str(0))
        if master_mode:
            self.status.appendPlainText("----------------------------------------")
            self.status.appendPlainText("Passwords module: " + str(active_passwords_module))
        self.mini_text_lable = QPlainTextEdit(self)
        self.mini_text_lable.setReadOnly(True)
        first_button = QPushButton("Command", self)
        first_button.clicked.connect(self.task)
        self.block_for_anusual_information = QLineEdit()
        self.block_for_anusual_information.setAlignment(Qt.AlignTop)
        button_of_confirming_of_unusual_information = QPushButton("Send", self)
        button_of_confirming_of_unusual_information.clicked.connect(self.unusual_task)
        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(project)
        vbox_1.addWidget(avatar)
        vbox_2 = QVBoxLayout()
        vbox_2.addWidget(self.start_checking_of_our_chat_on_our_site_button)
        vbox_2.addWidget(self.voice_trigger)
        hbox_1 = QHBoxLayout()
        hbox_1.addLayout(vbox_1)
        hbox_1.addLayout(vbox_2)
        hbox_1.addWidget(self.status)
        hbox_2 = QHBoxLayout()
        vbox_3 = QVBoxLayout()
        vbox_3.addWidget(first_button)
        vbox_3.addWidget(self.block_for_anusual_information)
        vbox_3.addWidget(button_of_confirming_of_unusual_information)
        hbox_2.addLayout(vbox_3)
        hbox_2.addWidget(self.mini_text_lable)
        vbox_4 = QVBoxLayout()
        vbox_4.addLayout(hbox_1)
        vbox_4.addLayout(hbox_2)
        self.setLayout(vbox_4)

    @staticmethod
    def speak(audio_string):
        tts = gTTS(text=audio_string, lang="ru")
        random_key = random.randint(1, 1000000)
        audio_file = "audio-" + str(random_key) + ".mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)

    def record_audio(self, ask=False):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source, duration=1)
            if ask:
                self.speak(ask)
            audio = r.listen(source)
            voice_data = ''
            try:
                voice_data = r.recognize_google(audio, language="ru-RU").lower()
            except sr.UnknownValueError:
                self.speak("Простите, я не поняла")
            except sr.RequestError:
                self.speak("Сервер не найден")
            return voice_data

    def respond(self, decoded_translation):
        if ("новый пароль" in decoded_translation) and master_mode:
            count_of_message = 1
            if voice_is_on:
                self.speak("Для какого сервиса вам нужен пароль")
                self.mini_text_lable.appendPlainText("    " * count_of_message + "Athena: Для какого сервиса вам нужен пароль?")
                count_of_message += 1
                which_service_voice_data = self.record_audio()
                self.mini_text_lable.appendPlainText("    " * count_of_message + "Создатель: " + str(which_service_voice_data))
                count_of_message += 1
            else:
                self.mini_text_lable.appendPlainText("    " * count_of_message + "Athena: Для какого сервиса вам нужен пароль?")
                count_of_message += 1
                which_service_voice_data = "Temp"
            try_to_print_info_from_passwords_module = core_of_passwords_maker.make_new_password(which_service_voice_data)
            self.mini_text_lable.appendPlainText("    " * count_of_message + "Athena:" + str(try_to_print_info_from_passwords_module))
        elif ("сколько времени" in decoded_translation) or ("сейчас времени" in decoded_translation):
            our_temp_time = datetime.datetime.now()
            self.speak(str(our_temp_time))
            self.mini_text_lable.appendPlainText("    Athena:" + str(our_temp_time))
        elif "стоп" in decoded_translation:
            sys.exit()
        else:
            if voice_is_on:
                self.speak(decoded_translation)

    def str_to_tokens(self, sentence: str):
        words = sentence.lower().split()
        tokens_list = list()
        for word in words:
            tokens_list.append(self.tokenizer.word_index[word])
        return preprocessing.sequence.pad_sequences([tokens_list], maxlen=self.maxlen_questions,
                                                    padding="post")  # !--------------------------------

    def preparation_of_task(self, voice_data):
        self.mini_text_lable.appendPlainText("Создатель: " + voice_data)
        stop_condition = False
        decoded_translation = ''
        try:
            states_values = self.enc_model.predict(self.str_to_tokens(voice_data))
            empty_target_seq = np.zeros((1, 1))
            empty_target_seq[0, 0] = self.tokenizer.word_index["start"]
            while not stop_condition:
                dec_outputs, h, c = self.dec_model.predict([empty_target_seq] + states_values)
                sampled_word_index = np.argmax(dec_outputs[0, -1, :])
                sampled_word = None
                for word, index in self.tokenizer.word_index.items():
                    if sampled_word_index == index:
                        decoded_translation += " {}".format(word)
                        sampled_word = word
                if sampled_word == "end" or len(decoded_translation.split()) > self.maxlen_answers:
                    stop_condition = True
                empty_target_seq = np.zeros((1, 1))
                empty_target_seq[0, 0] = sampled_word_index
                states_values = [h, c]
            self.mini_text_lable.appendPlainText("    Athena:" + decoded_translation[:-3])
            self.respond(decoded_translation[:-3])
        except KeyError:
            self.respond(voice_data.lower())

    def task(self):
        if self.is_it_first_task:
            if voice_is_on:
                self.speak("Здраствуйте, что я могу для вас сделать")
                self.mini_text_lable.appendPlainText("    Athena: Здраствуйте, что я могу для вас сделать?")
            self.is_it_first_task = False
        voice_data = self.record_audio()
        self.preparation_of_task(voice_data)
        self.status_updater()

    def unusual_task(self):
        text_task_from_user = str(self.block_for_anusual_information.text())
        self.block_for_anusual_information.setText('')
        self.preparation_of_task(text_task_from_user)
        self.status_updater()

    def status_updater(self):
        self.status.clear()
        self.status.appendPlainText("Data and time of execution: " + str(self.date_and_time_of_start))
        self.status.appendPlainText("Data and time of the last status update: " + str(datetime.datetime.now()))
        self.status.appendPlainText("Voice answering: " + str(self.voice_trigger.text()[9:]))
        self.status.appendPlainText("You are master: " + str(master_mode))
        self.status.appendPlainText("Internet chat module: " + str(active_chat_module))
        self.status.appendPlainText("Data and time of the last database check: " + str(0))
        if master_mode:
            self.status.appendPlainText("----------------------------------------")
            self.status.appendPlainText("Passwords module: " + str(active_passwords_module))
            if active_passwords_module:
                self.speak("Создатель, у вас всё ещё открыт модуль паролей, в защитных целях рекомендуется закрыть его")
                self.mini_text_lable.appendPlainText("Athena: Создатель, у вас всё ещё открыт модуль паролей! "
                                                     "В защитных целях рекомендуется закрыть его.")

    def voice_triggering(self):
        global voice_is_on
        if self.voice_trigger.text() == "Voice is ON":
            voice_is_on = False
            self.voice_trigger.setText("Voice is OFF")
            self.status_updater()
        else:
            voice_is_on = True
            self.voice_trigger.setText("Voice is ON")
            self.status_updater()

    def start_checking_of_our_chat_on_our_site(self):
        if self.start_checking_of_our_chat_on_our_site_button.text() == "Start Chat Checking":
            self.start_checking_of_our_chat_on_our_site_button.setText("Stop Chat Checking")
        else:
            self.start_checking_of_our_chat_on_our_site_button.setText("Start Chat Checking")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfOurApp()
    program.show()
    sys.exit(application.exec_())
