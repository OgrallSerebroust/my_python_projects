import sys
import numpy as np
import matplotlib.pyplot as plt
from math import fabs
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import Qt, QSize

xs_for_plot = []
answers_for_plot = []
xs_for_analytics_plot = []
answers_for_analytics_plot = []
plt.style.use("classic")

class Main_part_of_our_app(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		styleshit = '''
		.QLabel
		{
			margin:0;
			padding:0;
			background-color:rgba(0, 0, 0, 0.7);
			color:#FFFFFF;
			font:14pt EagleSans-Bold;
			border:3px solid #0AF3FF;
			border-radius:5px;
		}
		
		.QLineEdit
		{
			margin:0;
			padding:0;
			background-color:rgba(0, 0, 0, 0.7);
			color:#FFFFFF;
			font:14pt EagleSans-Bold;
			border:3px solid #0AF3FF;
			border-radius:5px;
		}
		
		.QPushButton
		{
			margin:0;
			padding:0;
			background-color:#0AF3FF;
			color:#FFFFFF;
			font:14pt EagleSans-Bold;
			border-radius:5px;
		}
		
		.QPushButton:hover
		{
			background-color:#04B0BB;
		}
		'''
		our_task = QLabel("Требуется решить: ∫t²arccos(xt)dt", self)
		about_a = QLabel("Уважаемый пользователь, пожалуйста, введите <i><b>нижний</b></i> предел интегрирования: ", self)
		self.a_equal = QLineEdit()
		self.a_equal.setFocus()
		about_b = QLabel("Уважаемый пользователь, пожалуйста, введите <i><b>верхний</b></i> предел интегрирования: ", self)
		self.b_equal = QLineEdit()
		about_x = QLabel("Пожалуйста, укажите пределы, в которых находится x...", self)
		about_x_line_2 = QLabel("x принадлежит интервалу от..., до...")
		self.min_x_equal = QLineEdit()
		self.max_x_equal = QLineEdit()
		number_of_parts_question = QLabel("Введите, пожалуйста, количество отрезков разбиения интеграла: ", self)
		self.number_of_parts = QLineEdit()
		self.number_of_parts.returnPressed.connect(self.calculation)
		then_number_of_parts_text = QLabel("Тогда, шаг разбиения: ", self)
		self.then_number_of_parts = QLabel(self)
		f_answer_text = QLabel("Значение данного интеграла при заданном разбиении: ", self)
		button_confirm = QPushButton("Рассчитать", self)
		button_confirm.clicked.connect(self.calculation)
		self.checkbox_of_visuality = QCheckBox(self)
		label_of_visuality = QLabel("Отрисовка графиков(Да/Нет)", self)
		#button_confirm.resize(button_confirm.sizeHint())
		self.f_answer = QLabel(self)
		self.f_answer.setStyleSheet('''
			min-width:1000px;
			min-height:600px;
			background-color:#FFFFFF;
		''')
		then_difference = QLabel("Итак, максимальная невязка между аналитическим и числовым решениями равна: ", self)
		self.then_difference_answer = QLabel(self)
		hbox_1 = QHBoxLayout()
		hbox_1.addStretch(1)
		hbox_1.addWidget(self.f_answer)
		hbox_1.addStretch(1)
		hbox_2 = QHBoxLayout()
		hbox_2.addWidget(f_answer_text)
		hbox_2.addWidget(button_confirm)
		hbox_2.addWidget(self.checkbox_of_visuality)
		hbox_2.addWidget(label_of_visuality)
		hbox_3 = QHBoxLayout()
		hbox_3.addWidget(then_number_of_parts_text)
		hbox_3.addWidget(self.then_number_of_parts)	
		hbox_4 = QHBoxLayout()
		hbox_4.addWidget(number_of_parts_question)
		hbox_4.addWidget(self.number_of_parts)
		hbox_5 = QHBoxLayout()
		hbox_5.addWidget(about_b)
		hbox_5.addWidget(self.b_equal)
		hbox_6 = QHBoxLayout()		
		hbox_6.addWidget(about_a)
		hbox_6.addWidget(self.a_equal)
		hbox_7 = QHBoxLayout()
		hbox_7.addWidget(about_x_line_2)
		hbox_7.addWidget(self.min_x_equal)
		hbox_7.addWidget(self.max_x_equal)
		vbox = QVBoxLayout()
		vbox.addWidget(our_task)
		vbox.addWidget(about_x)
		vbox.addLayout(hbox_7)
		vbox.addLayout(hbox_6)
		vbox.addLayout(hbox_5)
		vbox.addLayout(hbox_4)
		vbox.addLayout(hbox_3)
		vbox.addLayout(hbox_2)
		vbox.addLayout(hbox_1)
		vbox.addWidget(then_difference)
		vbox.addWidget(self.then_difference_answer)
		oImage = QImage("oformlenie/6.jpg")
		sImage = oImage.scaled(QSize(1600, 900))
		palette = QPalette()
		palette.setBrush(QPalette.Window, QBrush(sImage))
		self.setPalette(palette)
		self.showMaximized()
		self.setWindowFlags(Qt.WindowCloseButtonHint)
		self.setLayout(vbox)
		self.setWindowIcon(QIcon("icon_2.png"))
		self.setWindowTitle("Нахождение интеграла")
		self.setStyleSheet(styleshit)
		self.center()
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	def calculation(self):
		a = float(self.a_equal.text())
		b = float(self.b_equal.text())
		min_x = float(self.min_x_equal.text())
		max_x = float(self.max_x_equal.text())
		if(min_x > max_x):
			min_x, max_x = max_x, min_x
		#print("a = " + str(a))
		#print("b = " + str(b))
		#print("min x = " + str(min_x))
		#print("max x = " + str(max_x))
		n = float(self.number_of_parts.text())
		h = (b - a) / n
		#x_i = min_x
		total_f = 0
		#while(x_i <= 1.0):
		temp1 = []
		for i in range(0, 20):
			x_new = min_x + float(i) * ((max_x - min_x) / 20.0)
			for j in range(1, int(n) + 1):
				t_i = a + float(j) * h
				f = (t_i ** 2) * np.arccos(t_i * x_new)
				total_f += f
			answers_for_plot.append(total_f * h)
			xs_for_plot.append(x_new)
			total_f = 0
		min_x = float(self.min_x_equal.text())
		self.work(h, answers_for_plot, n, min_x, max_x)
	def making_plot(self, answers_for_plot, xs_for_analytics_plot, answers_for_analytics_plot, n):
		fig = plt.figure(figsize = (10, 6), dpi = 80)
		ax = plt.axes(alpha = 0.3)
		plt.plot(xs_for_plot, answers_for_plot, color = "#0af3ff")
		plt.scatter(xs_for_plot, answers_for_plot, c = "#0000CC")
		plt.plot(xs_for_analytics_plot, answers_for_analytics_plot, color = "#ffd115")
		plt.scatter(xs_for_analytics_plot, answers_for_analytics_plot, c = "#93780c")
		plt.xlim(-1.1, 1.1)
		if(n < 24):
			plt.xticks(xs_for_plot, rotation = 45)
		if(n < 16):
			#plt.yticks(answers_for_analytics_plot)
			plt.yticks(answers_for_plot)
		plt.ylabel("Значения интеграла")
		plt.grid(color = "#000000", linestyle = "solid")
		xs_for_plot.clear()
		answers_for_plot.clear()
		xs_for_analytics_plot.clear()
		answers_for_analytics_plot.clear()
		fig.savefig("temp_pic.png")
	def calculation_by_analytics(self, h, answers_for_plot, n, min_x, max_x):
		x_i_for_analytics = min_x
		try:
			old_file_with_answers = open("answers_by_analytics/" + str(int(n)) + ".txt", "r")
			for answers_for_analytics_plot_from_old_file_with_answers in old_file_with_answers:
				answers_for_analytics_plot.append(float(answers_for_analytics_plot_from_old_file_with_answers))
			with open("xs_by_analytics/" + str(int(n)) + ".txt", "r") as old_file_with_xs:
				for xs_for_analytics_plot_from_old_file in old_file_with_xs:
					xs_for_analytics_plot.append(float(xs_for_analytics_plot_from_old_file))
		except FileNotFoundError:
			print("Koroche schitaem...")
			with open("answers_by_analytics/" + str(int(n)) + ".txt", "w") as new_file_with_answers:
				for i in range (0, 20):
					x_i_for_analytics = min_x + i * ((max_x - min_x) / 20)
					if((x_i_for_analytics == 0.0) or (x_i_for_analytics < h / 2 and x_i_for_analytics > - h / 2) or (x_i_for_analytics > - h / 2 and x_i_for_analytics < h / 2)):
						answer_by_analytics_function = 0.523598775598299
					else:
						answer_by_analytics_function = (2.0 / (9 * (x_i_for_analytics ** 3))) - ((((np.sqrt(1 - (x_i_for_analytics ** 2))) * ((x_i_for_analytics ** 2) + 2)) - ((3 * (x_i_for_analytics ** 3)) * np.arccos(x_i_for_analytics))) / (9 * (x_i_for_analytics ** 3)))
					answer_for_new_file_with_answers = answer_by_analytics_function
					new_file_with_answers.write(str(answer_for_new_file_with_answers) + "\n")
					answers_for_analytics_plot.append(answer_by_analytics_function)
					xs_for_analytics_plot.append(x_i_for_analytics)
				with open("xs_by_analytics/" + str(int(n)) + ".txt", "w") as new_file_with_xs:
					for xs_for_analytics_plot_for_new_file in xs_for_analytics_plot:
						new_file_with_xs.write(str(xs_for_analytics_plot_for_new_file) + "\n")
		self.calculation_of_difference(answers_for_plot, answers_for_analytics_plot)
		self.making_plot(answers_for_plot, xs_for_analytics_plot, answers_for_analytics_plot, n)
	def calculation_of_difference(self, answers_for_plot, answers_for_analytics_plot):
		max_difference = 0
		try:
			for i in range(0, len(answers_for_analytics_plot)):
				difference_in_step = fabs(answers_for_plot[i] - answers_for_analytics_plot[i])
				if(difference_in_step > max_difference):
					max_difference = difference_in_step
		except IndexError:
			for i in range(0, len(answers_for_plot)):
				difference_in_step = fabs(answers_for_plot[i] - answers_for_analytics_plot[i])
				if(difference_in_step > max_difference):
					max_difference = difference_in_step
		#print(answers_for_plot)
		#print("___________________________________")
		#print(answers_for_analytics_plot)
		#print(max_difference)
		self.then_difference_answer.setText("%.100f" %max_difference)
	def work(self, h , answers_for_plot, n, min_x, max_x):
		self.then_number_of_parts.setText("%.100f" %h)
		self.calculation_by_analytics(h, answers_for_plot, n, min_x, max_x)
		pixmap = QPixmap("temp_pic.png")
		self.f_answer.setPixmap(pixmap)
if __name__ == '__main__':
	application = QApplication(sys.argv)
	program = Main_part_of_our_app()
	program.show()
	sys.exit(application.exec_())
