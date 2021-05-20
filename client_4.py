import socket
import util
from enum import Enum

PORT = 9993
ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)

# Recieve the two file sizes
msg = util.recieve_and_format(sck)
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
util.encode_and_send(str(ratio), sck)

# Get the flag
flag = util.recieve_and_format(sck)
print(flag)
sck.close()

'''
Citation:
https://docs.python.org/3/library/enum.html
'''