import socket
import util
import math

LIMIT = math.pow(2,8)
PORT = 9999
ADDRESS = (util.SERVER,PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)

# Receive the string representantion of the first & second byte
string_representation = util.recieve_and_format(sck)
print(string_representation)
a, b = string_representation.split(" ")

def checksum(a, b):
    a = int(a, 2)
    b = int(b, 2)
    a = a + b
    if (a > LIMIT):
        a -= LIMIT
        a += 1
    out = ""
    for i in range(7, -1, -1):
        if a >= math.pow(2,i):
            out += '0'
            a -= math.pow(2,i)
        else:
            out += '1'
    return out

#send back the internet checksum as a string
msg = checksum(a, b)
print(msg)
util.encode_and_send(msg,sck)

# Receive the flag
flag = util.recieve_and_format(sck)
print(flag)

sck.close()