import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use("seaborn-deep")

mass_with_all_main_pointers_coordinates = np.array([[[1], [1], [1]], [[99], [1], [1]], [[50], [99], [1]], [[50], [50], [99]]])
list_with_all_our_pointers = []
list_with_xs_for_plot_from_list_with_all_our_pointers = []

temp_mass_1 = np.arange(100)
temp_mass_2 = np.zeros(100)
temp_mass_3 = np.linspace(0, 50, 100)
temp_mass_4 = np.linspace(100, 50, 100)
temp_mass_5 = np.linspace(50, 50, 100)

mass_with_x_coordinates_for_main_points = np.array([[1], [99], [50]])
mass_with_y_coordinates_for_main_points = np.array([[1], [1], [99]])
mass_with_z_coordinates_for_main_points = np.array([[1], [1], [1]])

figure = plt.figure()
axes = figure.add_subplot(111, projection = "3d")
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_zlabel('Z Label')

for i in range(0, 4):
	#axes.scatter(mass_with_all_main_pointers_coordinates[i, 0], mass_with_all_main_pointers_coordinates[i, 1], mass_with_all_main_pointers_coordinates[i, 2], zdir = "z", c = "#000000", depthshade = True)
	list_with_all_our_pointers.append(mass_with_all_main_pointers_coordinates[i])
print(list_with_all_our_pointers)
axes.plot(temp_mass_1, temp_mass_2, temp_mass_2, color = "#000000")
axes.plot(temp_mass_3, temp_mass_1, temp_mass_2, color = "#000000")
axes.plot(temp_mass_4, temp_mass_1, temp_mass_2, color = "#000000")
axes.plot(temp_mass_3, temp_mass_3, temp_mass_1, color = "#000000")
axes.plot(temp_mass_4, temp_mass_3, temp_mass_1, color = "#000000")
axes.plot(temp_mass_5, temp_mass_4, temp_mass_1, color = "#000000")
B0 = np.array([[np.random.randint(0, 100)], [np.random.randint(0, 100)], [np.random.randint(0, 100)]])
list_with_all_our_pointers.append(B0)
print(list_with_all_our_pointers)
#axes.scatter(B0[0], B0[1], B0[2], zdir = "z", s = 1, c = "#0000FF", depthshade = True)

for i in range(0, 40000):
	index_of_random_top_pointer = np.random.randint(0, 4)
	random_top_pointer = mass_with_all_main_pointers_coordinates[index_of_random_top_pointer]
	#random_top_pointer = [mass_with_x_coordinates_for_main_points[index_of_random_top_pointer], mass_with_y_coordinates_for_main_points[index_of_random_top_pointer]]
	B1 = np.array([[(random_top_pointer[0] + B0[0])/2], [(random_top_pointer[1] + B0[1]) / 2], [(random_top_pointer[2] + B0[2]) / 2]])
	list_with_all_our_pointers.append(B1)
	#axes.scatter(B1[0], B1[1], B1[2], s = 1, c = "#0000FF")
	B0 = B1
for mass in range(0, 100):
		list_with_xs_for_plot_from_list_with_all_our_pointers.append(list_with_all_our_pointers[mass][0])
print(list_with_xs_for_plot_from_list_with_all_our_pointers)
#plt.scatter(9, 1, 0, c = "#FF0000")
#plt.scatter(5, 9, 0, c = "#FF0000")
plt.show()