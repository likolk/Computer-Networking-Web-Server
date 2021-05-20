FORMAT = "UTF-8"
SERVER = "10.40.0.46"

# Recieve a response from the socket and format it with utf-8
def recieve_and_format(socket):
    data = socket.recv(1024)
    return str(data, FORMAT).rstrip("\r\n")

# Encode a string with utf-8 and send it to the socket
def encode_and_send(str, client):
    msg = str.encode(FORMAT)
    client.send(msg)