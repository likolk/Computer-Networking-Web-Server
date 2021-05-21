FORMAT = "UTF-8"
SERVER = "10.40.0.46"

def recieve_and_format(socket, l = 1024):
    """
    Recieve a response from the socket and format it with utf-8
    """
    data = socket.recv(l)
    return str(data, FORMAT).rstrip("\r\n")

def encode_and_send(str, socket):
    """
    Encode a string with utf-8 and send it to the socket
    """
    msg = str.encode(FORMAT)
    socket.send(msg)