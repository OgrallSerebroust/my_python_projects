import sys

def Printing_of_our_brackets_open_close(count_of_numeric_expressions):
	old_count_of_numeric_expressions = count_of_numeric_expressions
	
	if(count_of_numeric_expressions > 0):
		print("(", end = "")
		if(count_of_numeric_expressions > 1):
			Printing_of_our_brackets_open_close(count_of_numeric_expressions - 1)
		print(")", end = "")
	return old_count_of_numeric_expressions 

def Printing_of_our_brackets_open_close_open_close(count_of_numeric_expressions):
	#old_count_of_numeric_expressions = count_of_numeric_expressions
		
	if(count_of_numeric_expressions > 0):
		print("()", end = "")
		if(count_of_numeric_expressions > 1):
			Printing_of_our_brackets_open_close_open_close(count_of_numeric_expressions - 1)
	#return old_count_of_numeric_expressions

def Printing_of_our_brackets_open_close_open_close_in_open_close(count_of_numeric_expressions):
	#old_count_of_numeric_expressions = count_of_numeric_expressions
	print("(", end = "")
	Printing_of_our_brackets_open_close_open_close(count_of_numeric_expressions - 1)
	print(")", end = "")
	#return old_count_of_numeric_expressions

def Printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing(count_of_numeric_expressions):
	count_of_numeric_expressions = Printing_of_our_brackets_open_close(count_of_numeric_expressions - 1)
	temp_count_of_numeric_expressions = old_count_of_numeric_expressions - count_of_numeric_expressions
	Printing_of_our_brackets_open_close_open_close(temp_count_of_numeric_expressions)
	if(count_of_numeric_expressions > 2):
		print("\n")
		Printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing(count_of_numeric_expressions)
	#return old_count_of_numeric_expressions
	
def Printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa(highter_steps_of_recurtion_for_printing_first_part_in_printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa):
	#Printing_of_our_brackets_open_close_open_close(1) #!__________________________________________________________________________________________________________________________________
	#temp_count_of_numeric_expressions = old_count_of_numeric_expressions - 1
	#Printing_of_our_brackets_open_close(temp_count_of_numeric_expressions)
	#return old_count_of_numeric_expressions
	Printing_of_our_brackets_open_close_open_close(highter_steps_of_recurtion_for_printing_first_part_in_printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa)
	print(highter_steps_of_recurtion_for_printing_first_part_in_printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa)
	temp_count_of_numeric_expressions = old_count_of_numeric_expressions - highter_steps_of_recurtion_for_printing_first_part_in_printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa
	Printing_of_our_brackets_open_close(temp_count_of_numeric_expressions)
	if(highter_steps_of_recurtion_for_printing_first_part_in_printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa < old_count_of_numeric_expressions):
		print(highter_steps_of_recurtion_for_printing_first_part_in_printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa, old_count_of_numeric_expressions)
		Printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa(highter_steps_of_recurtion_for_printing_first_part_in_printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa)

sys.setrecursionlimit(10000)
Putin = True
while Putin:
	print("Доброго времени суток, многоуважаемый пользователь!\nДанная программа выводит определённое количество логически верных скобочных выражений")
	try:
		count_of_numeric_expressions = int(input("Пожалуйста, введите количество скобочных выражений, которое необходимо отобразить: "))
		old_count_of_numeric_expressions = count_of_numeric_expressions
		highter_steps_of_recurtion_for_printing_first_part_in_printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa = 1
		if count_of_numeric_expressions == 0:
			Putin = False
		else:
			print("\n")
			count_of_numeric_expressions = Printing_of_our_brackets_open_close(old_count_of_numeric_expressions)
			print("\n")
			count_of_numeric_expressions = Printing_of_our_brackets_open_close_open_close(old_count_of_numeric_expressions)
			print("\n")
			count_of_numeric_expressions = Printing_of_our_brackets_open_close_open_close_in_open_close(old_count_of_numeric_expressions)
			print("\n")
			count_of_numeric_expressions = Printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing(old_count_of_numeric_expressions)
			print("\n")
			count_of_numeric_expressions = Printing_of_our_brackets_open_close_in_open_close_with_other_opening_closing_vice_versa(old_count_of_numeric_expressions)
			print("\n")
	except ValueError:
		print("Вводить можно только цифры...")