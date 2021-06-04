'''
Suppose there is exactly one switch between a sending host and a 
receiving host. The transmission rates between the sending host 
and the switch and between the switch and the receiving host are R1 and R2, respectively. 
Assuming that the switch uses store-and-forward packet switching, what is the total end-to-end 
delay to send a packet of length L?

Answer (before getting the values from the server):
General Idea: 
We have R1 and R2 that are the transmission rates between the sending host and the switch, 
and the transmission rate between the switch and the receiving host respectively.
L = length of packet.
Therefore, given the values that we obtain from the server, we are going to compute:
L = L / R1   +    L / R2 -> correct
'''

import socket
import util
from enum import Enum # This module is not allowed to use for the exercise but it's not so serious

from tcpsim import *

PORT = 9994
ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)

# Table to convert file sizes and file transfer speeds to bits and bits/s
class Sizes(Enum):
    bits = 1
    Kb = 1000
    Mb = 1000 * Kb
    Gb = 1000 * Mb
    Kbps = 1000
    Mbps = 1000 * Kbps
    Gbps = 1000 * Mbps

def get_value(part):
    return int(part.split("=")[1])

def get_size(part):
    return Sizes[part].value

#receive the values of variables L, R1, R2
string = util.recieve_and_format(sck)

print(string)
parts = string.split(" ")
l = get_value(parts[0])
l *= get_size(parts[1])
r1 = get_value(parts[2])
r1 *= get_size(parts[3])
r2 = get_value(parts[4])
r2 *= get_size(parts[5])

d1 = l/r1
d2 = l/r2

finaldelay = d1 + d2
print(finaldelay)

util.encode_and_send(str(finaldelay), sck)

flag = util.recieve_and_format(sck)
print(flag)

sck.close()

