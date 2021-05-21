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
L = L / R1   +    L / R2 
'''

import socket
import util

from tcpsim import *


PORT = 9994

ADDRESS = (util.SERVER,PORT)

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sck.connect(ADDRESS)


#receive the values of variables L, R1, R2

L = util.recieve_and_format(sck)
R1 = util.recieve_and_format(sck)
R2 = util.recieve_and_format(sck)

d1 = L/R1
d2 = L/R2


finaldelay = d1 + d2

util.encode_and_send(finaldelay, sck)


flag = util.recieve_and_format(sck)

print(flag)

sck.close()

