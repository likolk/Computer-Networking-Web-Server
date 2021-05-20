import socket
from enum import Enum

FORMAT = "UTF-8"
SERVER = "10.40.0.46"
PORT = 9993
ADDRESS = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

# Recieve the two file sizes
data = client.recv(1024)
msg = str(data, FORMAT).rstrip("\r\n")
print(msg)

# Split the message in 4 words and identify the file sizes
words = msg.split(" ")
file_1 = words[:2]
file_2 = words[-2:]

# Table to convert file sizes to Kbit
class Sizes(Enum):
    Kibit = 1.024
    Mibit = 1024 * Kibit
    Gibit = 1024 * Mibit
    Kbit = 1
    Mbit = 1000 * Kbit
    Gbit = 1000 * Mbit

# Function to find size of a file in Kbits
def get_size(file):
    size = int(file[0])
    size *= Sizes[file[1]].value
    return size

# Find the ratio between the first file and the second file
size_1 = get_size(file_1)
size_2 = get_size(file_2)
ratio = size_1/size_2
print(ratio)

# Send back the result
msg = str(ratio).encode(FORMAT)
client.sendto(msg, ADDRESS)

# Get the flag
datagram = client.recv(1024)
flag = str(datagram, FORMAT).rstrip("\r\n")
print(flag)
client.close()

'''
Citation:
https://docs.python.org/3/library/enum.html
'''