import socket
import util

# This program uses code from the tcpsim file to parse and make simulated TCP messages
from tcpsim import *

PORT = 9995

ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)

# Send the first string
msg = make_string(SYN_STR, {SEQ_VALUE: 0})
print(msg)
util.encode_and_send(msg, sck)

# Recieve the second string
res = util.recieve_and_format(sck)
print(res)

# Create seq and ack numbers for third string
values = parse_string(res)
values = next_segment(values)

# Send the third string
msg = make_string(ACK_STR, values)
print(msg)
util.encode_and_send(msg, sck)

# Recieve the flag
flag = util.recieve_and_format(sck)
print(flag)
sck.close()