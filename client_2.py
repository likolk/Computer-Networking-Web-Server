import socket

# send

FORMAT = "UTF-8"
SERVER = "10.40.0.46"
PORT = 9991
MESSAGE_STR = "helo"
MESSAGE  = MESSAGE_STR.encode(FORMAT)


DISCONNECT_MESSAGE = "!DC"

ADDRESS = (SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.sendto(MESSAGE, (SERVER, PORT))
print(MESSAGE_STR)

#receive 

datagram, address = sck.recvfrom(1024)
flag = str(datagram, FORMAT).rstrip("\n")
print(flag)


'''
Citation:
https://wiki.python.org/moin/UdpCommunication


Citation:
https://www.youtube.com/watch?v=BlQbUV_W954
https://www.youtube.com/watch?v=3QiPPX-KeSc
'''






















