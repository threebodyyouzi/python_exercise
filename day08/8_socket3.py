import socket
import time

host=""
port=12345
addr=(host,port)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)
while True:
    try:
        cli_sock,cli_addr=s.accept()
    except KeyboardInterrupt:
        break
    print("Welcome to my Chatroom",cli_addr)
    while True:
        try:
            data=cli_sock.recv(1024).decode()
        except (UnicodeDecodeError,KeyboardInterrupt):
            break
        if data.strip()=="":
            break
        data=data.strip()+"        "+time.strftime("%Y-%m-%d %H:%M:%S")
        print(data)
        s_data=input(">")+"        "+time.strftime("%Y-%m-%d %H:%M:%S")+"\r\n"
        cli_sock.send(s_data.encode())

    cli_sock.close()
s.close()