import socket
import util
import random as rand

# This program uses code from the tcpsim file to parse and make simulated TCP messages
from tcpsim import *

PORT = 9996
FLAGS = (FIN_STR, ACK_STR)

RANGE_END = 15

# Randomize the first Seq and Ack values
random = {}
random[SEQ_VALUE] = rand.randrange(RANGE_END)
random[ACK_VALUE] = rand.randrange(RANGE_END)

ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)

# Send the first string
msg = make_string(FLAGS, random)
print(msg)
util.encode_and_send(msg, sck)

# Recieve the second and third string
res = util.recieve_and_format(sck)
res_1, res_2 = res.split('\n')
print(res)

# Create seq and ack numbers for fourth string
values = parse_string(res_2)
values = next_segment(values)

# Send the fourth string
msg = make_string(ACK_STR, values)
print(msg)
util.encode_and_send(msg, sck)

# Recieve the flag
flag = util.recieve_and_format(sck)
print(flag)
sck.close()