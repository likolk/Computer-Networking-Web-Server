import socket

FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DC"
SERVER = "10.40.0.46"
PORT = 9990
ADDRESS = (SERVER, PORT)
ΗEADER = 128
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)









''' 
Citation:
https://www.youtube.com/watch?v=BlQbUV_W954
https://www.youtube.com/watch?v=3QiPPX-KeSc
'''