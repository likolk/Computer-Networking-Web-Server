import socket

FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DC"
SERVER = "10.40.0.46"
PORT = 9992
ADDRESS = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
data = client.recv(1024)
msg = str(data, FORMAT).rstrip("\r\n")
print(msg)

# We get the port as the last 5 characters of the message
# and turn that into an integer
new_port = int(msg[-5:])
client.close()

# Connect for the 2nd time

ADDRESS_NEW = (SERVER, new_port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS_NEW)

data = client.recv(1024)
msg = str(data, FORMAT).rstrip("\r\n")
print(msg)
client.close()
