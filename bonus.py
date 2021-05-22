import socket
import util
import importlib
import sys
import time

if len(sys.argv) < 2:
    exit("Missing username")

USERNAME = sys.argv[1]
PORT = 11111
ADDRESS = (util.SERVER,PORT)

def get_string(n):
    def get_file_name(n):
        return "client_" + str(n)

    def get_flag(file_name):
        module = importlib.import_module(file_name)
        flag = module.flag
        del module
        return flag 

    return USERNAME + " " + str(n) + " " + get_flag(get_file_name(n))

for i in range(1, 11):
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.connect(ADDRESS)

    string = get_string(i)
    print(string)
    util.encode_and_send(string,sck)
    print(util.recieve_and_format(sck))

    sck.close()
    time.sleep(1)
