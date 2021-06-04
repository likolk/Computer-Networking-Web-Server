import socket
import util

DISCONNECT_MESSAGE = "!DC" # You defined it but never use 
PORT = 9992
ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)
msg = util.recieve_and_format(sck)
print(msg)

# We get the port as the last 5 characters of the message
# and turn that into an integer
new_port = int(msg[-5:])
sck.close()

# Connect for the 2nd time

ADDRESS_NEW = (util.SERVER, new_port)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS_NEW)

flag = util.recieve_and_format(sck)
print(flag)
sck.close()
