import socket

FORMAT = "UTF-8"
SERVER = "10.40.0.46"
PORT = 9991
MESSAGE  = "helo"


DISCONNECT_MESSAGE = "!DC"

ADDRESS = (SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.sendto(MESSAGE, (SERVER, PORT))



SERVER = "10.40.0.46"
PORT = 9991
sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.bind(SERVER, PORT)
while (True):
    data, addr = sck.recvfrom(1024)
    print('received message is: ' + data)





'''
Citation:
https://wiki.python.org/moin/UdpCommunication


Citation:
https://www.youtube.com/watch?v=BlQbUV_W954
https://www.youtube.com/watch?v=3QiPPX-KeSc
'''






















