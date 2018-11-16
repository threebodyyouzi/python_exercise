import sys
import socket
def communicate(cli_sock):
    while True:
        try:
            data =input(">")+"\r\n"
        except:
            print()
            break
        else:
            cli_sock.send(data.encode())
            if data.strip()=="quit":
                break
            print(cli_sock.recv(1024).decode())
    pass

if __name__ == '__main__':
    host=sys.argv[1]
    port=int(sys.argv[2])
    addr=(host,port)
    c=socket.socket()
    c.connect(addr)
    communicate(c)
    c.close()