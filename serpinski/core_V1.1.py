import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use("dark_background")

mass_with_100_numbers_0_100 = np.arange(100)
mass_with_100_0 = np.zeros(100)
mass_with_100_numbers_0_50 = np.linspace(0, 50, 100)
mass_with_100_numbers_100_50 = np.linspace(100, 50, 100)
mass_with_100_100 = np.linspace(100, 100, 100)
mass_with_all_x_coordinates_for_all_points = [1, 99, 99, 50, 1]
mass_with_all_y_coordinates_for_all_points = [1, 1, 99, 50, 99]
mass_with_all_z_coordinates_for_all_points = [1, 1, 1, 99, 1]
x_for_b0 = np.random.randint(0, 100)
y_for_b0 = np.random.randint(0, 100)
z_for_b0 = np.random.randint(0, 100)

figure = plt.figure()
axes = figure.add_subplot(111, projection = "3d")
axes.set_xlabel('')
axes.set_ylabel('')
axes.set_zlabel('')
axes.plot(mass_with_100_numbers_0_100, mass_with_100_0, mass_with_100_0, color = "#00FF00")
axes.plot(mass_with_100_0, mass_with_100_numbers_0_100, mass_with_100_0, color = "#00FF00")
axes.plot(mass_with_100_100, mass_with_100_numbers_0_100, mass_with_100_0, color = "#00FF00")
axes.plot(mass_with_100_numbers_0_100, mass_with_100_100, mass_with_100_0, color = "#00FF00")
axes.plot(mass_with_100_numbers_0_50, mass_with_100_numbers_0_50, mass_with_100_numbers_0_100, color = "#00FF00")
axes.plot(mass_with_100_numbers_100_50, mass_with_100_numbers_0_50, mass_with_100_numbers_0_100, color = "#00FF00")
axes.plot(mass_with_100_numbers_0_50, mass_with_100_numbers_100_50, mass_with_100_numbers_0_100, color = "#00FF00")
axes.plot(mass_with_100_numbers_100_50, mass_with_100_numbers_100_50, mass_with_100_numbers_0_100, color = "#00FF00")

mass_with_all_x_coordinates_for_all_points.append(x_for_b0)
mass_with_all_y_coordinates_for_all_points.append(y_for_b0)
mass_with_all_z_coordinates_for_all_points.append(z_for_b0)
number_of_points = int(input("Дорогой пользователь, пожалуйста введите количество точек, используемых при отрисовке нашей замечательной пирамиды: "))

for i in range(0, number_of_points):
	index_of_random_top_pointer = np.random.randint(0, 5)
	random_top_pointers_x_coordinat = mass_with_all_x_coordinates_for_all_points[index_of_random_top_pointer]
	random_top_pointers_y_coordinat = mass_with_all_y_coordinates_for_all_points[index_of_random_top_pointer]
	random_top_pointers_z_coordinat = mass_with_all_z_coordinates_for_all_points[index_of_random_top_pointer]
	x_for_b1 = (random_top_pointers_x_coordinat + x_for_b0) / 2
	y_for_b1 = (random_top_pointers_y_coordinat + y_for_b0) / 2
	z_for_b1 = (random_top_pointers_z_coordinat + z_for_b0) / 2
	mass_with_all_x_coordinates_for_all_points.append(x_for_b1)
	mass_with_all_y_coordinates_for_all_points.append(y_for_b1)
	mass_with_all_z_coordinates_for_all_points.append(z_for_b1)
	x_for_b0 = x_for_b1
	y_for_b0 = y_for_b1
	z_for_b0 = z_for_b1

axes.plot(mass_with_all_x_coordinates_for_all_points, mass_with_all_y_coordinates_for_all_points, mass_with_all_z_coordinates_for_all_points, marker = "o", color = "#370BFF", linestyle = "", markersize = 1)

plt.show()