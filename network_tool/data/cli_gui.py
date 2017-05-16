from tkinter import *
from socket import *


class ToolClient:
    def __init__(self, remote_ip):
        self.conn = self.initListenerSocket()
        self.sock = self.redirectIn()
        self.file = self.conn.makefile('r')
        self.remote_ip = remote_ip
        while True:
            data = self.file.readline().rstrip()
            print("1::%s" % data)

    def initListenerSocket(self, port=50008):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(5)
        conn, addr = sock.accept()
        return conn

    def redirectIn(self, port=50008):
        host = self.remote_ip
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        file = sock.makefile('r')
        sys.stdin = file
        return sock

if __name__ == "__main__":
    remote_ip = "192.168.1.69"
    cli = ToolClient(remote_ip)