import socket
import util
from httpsim import *

PORT = 9998

msg = Request("POST", "/", "HTTP/1.0")
msg.add_header("Host", host_header(util.SERVER, PORT))
msg.add_header("Content-Type", "application/text")
msg.set_body("")
str = msg.get_string()

ADDRESS = (util.SERVER, PORT)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(ADDRESS)

print(str, end="")
util.encode_and_send(str + "\r\n", sck)

res = Response(sck)
print(res.get_string())
# TODO