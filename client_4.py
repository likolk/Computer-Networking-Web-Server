


import socket


FORMAT = "UTF-8"



SERVER = "10.40.0.46"


PORT = 9993


ADDRESS = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(ADDRESS)