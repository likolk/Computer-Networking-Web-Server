import socket
import util
from httpsim import *

PORT = 9997

msg = Request("GET", "/", "HTTP/1.0")
msg.add_header("Host", host_header(util.SERVER, PORT))
str = msg.get_string()

ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)

print(str, end="")
util.encode_and_send(str, sck)

res = util.recieve_and_format(sck)
print(res)
# TODO