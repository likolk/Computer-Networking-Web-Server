import socket
import util

PORT = 9990
ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)
flag = util.recieve_and_format(sck)
print(flag)
sck.close()

''' 
Citation:
https://www.youtube.com/watch?v=BlQbUV_W954
https://www.youtube.com/watch?v=3QiPPX-KeSc
'''