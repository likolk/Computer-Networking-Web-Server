import socket

FORMAT = "UTF-8"

SERVER = "10.40.0.46"

PORT = 9999



ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



datagram = client.recv(1024)

flag = str(datagram, FORMAT).rstrip("\r\n")


#to find the checksum of the 2 8bit words, we add them
#and then apply 1's complement to the result aka flip all bits.

''' not finished
def checksum(msg):
    s = 0
    for i in range(0, len(msg)):
'''


print(flag)

client.close()