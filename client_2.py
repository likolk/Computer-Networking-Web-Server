import socket

# send

FORMAT = "UTF-8"
SERVER = "10.40.0.46"
PORT = 9991
MESSAGE_STR = "helo"
MESSAGE  = MESSAGE_STR.encode(FORMAT)

ADDRESS = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(MESSAGE, ADDRESS)
print(MESSAGE_STR)

#receive 

datagram = client.recv(1024)
flag = str(datagram, FORMAT).rstrip("\r\n")
print(flag)
client.close()

'''
Citation:
https://wiki.python.org/moin/UdpCommunication


Citation:
https://www.youtube.com/watch?v=BlQbUV_W954
https://www.youtube.com/watch?v=3QiPPX-KeSc
'''






















