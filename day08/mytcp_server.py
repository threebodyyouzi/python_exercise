import time
import socket
class TcpTimeserv():
    def __init__(self,host="",port=12345):
        self.addr=(host,port)
        self.serv=socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)
        self.serv.listen(1)
    def chat(self,cli_sock):
        while True:
            try :
                data=cli_sock.recv(1024).decode()
            except KeyboardInterrupt:
                print("guest has been kicked out")
                break
            except UnicodeDecodeError:
                break
            else:
                if data.strip()=="quit":
                    break
                data="[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"),data)
                print(data.rstrip())
                cli_sock.send(data.encode())
    def mainloop(self):
        while True:
            try:
                cli_sock,cli_addr=self.serv.accept()
            except KeyboardInterrupt:
                print()
                break
            self.chat(cli_sock)
            cli_sock.close()
        self.serv.close()
if __name__ == '__main__':
    tcp=TcpTimeserv()
    tcp.mainloop()