import socket
import util

# send
PORT = 9991
MESSAGE = "helo"

ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.connect(ADDRESS)
util.encode_and_send(MESSAGE, sck)
print(MESSAGE)

#receive 

flag = util.recieve_and_format(sck)
print(flag)
sck.close()

'''
Citation:
https://wiki.python.org/moin/UdpCommunication


Citation:
https://www.youtube.com/watch?v=BlQbUV_W954
https://www.youtube.com/watch?v=3QiPPX-KeSc
'''






















