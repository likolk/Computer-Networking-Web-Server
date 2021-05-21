import socket
import util
import math

from tcpsim import *


PORT = 9999


ADDRESS = (util.SERVER,PORT)


sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



sck.connect(ADDRESS)



# Receive the string representantion of the first & second byte

stringrepresentation = util.recieve_and_format(sck)
print(stringrepresentation)

#send back the internet checksum as a string


def checksum(num):
    # flip the bits aka 1's complement
    bit = ''
    inverse = ''
    for i in bit:
        if i == '0':
            inverse = inverse + '1'
        elif i == '1':
            inverse = inverse + '0'
        else:
            pass


            


    



msg = make_string(checksum) # if i add values here it does not compile, please have a look at it.
print(msg)
util.encode_and_send(msg,sck)

# Receive the flag
flag = util.recieve_and_format(sck)


#print the flag

print(flag)

#close socket
sck.close()






'''

Citation:
https://www.geeksforgeeks.org/different-ways-to-invert-the-binary-bits-in-python/
https://www.geeksforgeeks.org/invert-actual-bits-number/
'''