import socket

our_socket = socket.socket()

our_socket.connect(("localhost", 1488))
print("\nСОЕДИНЕНИЕ УСТАНОВЛЕНО!")
while True:
	data_from_user = str(input("\nДорогой пользователь, пожалуйста, введите ваш запрос:\n"))
	#our_socket.send(data_from_user)
	our_socket.send(bytes(data_from_user, encoding = "UTF - 8"))
	data = our_socket.recv(1024)
	print(data.decode("utf-8")[:-3])
our_socket.close()