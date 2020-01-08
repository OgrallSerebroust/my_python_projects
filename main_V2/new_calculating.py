import numpy as np
a, b, total_f, x_min, x_max = 0, 1, 0, -1.0, 1.0
answer = []
n = int(input("Введи n: "))
h = (b - a) / n
print("h = " + str(h))
#i = 1
while(x_min <= x_max):
	for i in range(1, int(n) + 1):
		x_i = a + i * h
		print("x = " + str(x_i))
		f_i = (-0.03 * (x_i ** 3)) + 0.26 * x_i - 0.26
		f_i =(x_i ** 2) * np.arccos(x_i * x_min)
		print("f = " + str(f_i))
		total_f += f_i
		print("__________________________")
	x_min += h
	answer.append(h * total_f)
	total_f = 0
print(answer)