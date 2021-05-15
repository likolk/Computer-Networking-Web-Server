import socket

FORMAT = "UTF-8"


DISCONNECT_MESSAGE = "!DC"


SERVER = "10.40.0.46"




PORT = 9992


ADDRESS = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(ADDRESS)









# Connect for the 2nd time
SERVER = "10.40.0.46"

# awaiting random_tcp_port 
 # PORT = .....



ADDRESS = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(ADDRESS)

