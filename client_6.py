import socket
import util

PORT = 9995
SYN_STR = "SYN"
ACK_STR = "ACK"
SEQ_VALUE = "Seq"
ACK_VALUE = "Ack"

# Create a simulated TCP message with the given flags, seq number and ack number
def make_string(flags, values):
    for value in values:
        flags += " " + value + "=" + str(values[value])
    return flags

# Parse a recieved string to get its "Seq" and "Ack" numbers
def parse_string(str):
    values = str.split(" ")
    out = {}
    for value in values:
        v = value.split("=")
        if (len(v) == 2):
            out[v[0]] = int(v[1])
    return out

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
values[SEQ_VALUE] = values[ACK_VALUE]

# Send the third string
msg = make_string(ACK_STR, values)
print(msg)
util.encode_and_send(msg, sck)

# Recieve the flag
flag = util.recieve_and_format(sck)
print(flag)
sck.close()