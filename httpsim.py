import util

CARRIAGE_RETURN = "\r\n"

class Request:
    def __init__(self, method, target, version):
        self.headers = ""
        self.body = ""
        self.str = method + " " + target + " " + version + CARRIAGE_RETURN

    def get_string(self):
        string = self.str + self.headers + CARRIAGE_RETURN + self.body
        return string

    def add_header(self, key, value):
        self.headers += key + ": " + value + CARRIAGE_RETURN

    def set_body(self, body):
        self.body = body
        self.add_header("Content-Length", str(len(body)))

def host_header(server, port):
    return server + ":" + str(port)

def read_line(socket):
    out = bytearray()
    s = socket.recv(1)
    out += s
    while s != b"\n":
        s = socket.recv(1)
        out += s
    return str(out, util.FORMAT)

class Response:
    def __init__(self, socket):
        self.str = read_line(socket)
        self.headers = ""
        s = read_line(socket)
        while s != "\r\n":
            self.headers += s
            s = read_line(socket)
        self.body = util.recieve_and_format(socket, 1024)

    def get_string(self):
        string = self.str + self.headers
        if len(self.body) > 0:
            string += CARRIAGE_RETURN + self.body
        return string

    def get_flag(self, flag_pos):
        return self.body.split(" ")[flag_pos].rstrip(CARRIAGE_RETURN)


