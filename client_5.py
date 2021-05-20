





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


FORMAT = "UTF-8"

SERVER = "10.40.0.46"

PORT = 9994

ADDRESS = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
data = client.recv(1024)
flag = str(data, FORMAT).rstrip("\r\n")
print(flag)
client.close

#not finished

