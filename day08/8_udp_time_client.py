import socket
host="127.0.0.1"
port=12345
addr=(host,port)
c=socket.socket(type=socket.SOCK_DGRAM)

while True:
    try:
        data=input(">")+"\r\n"
    except KeyboardInterrupt:
        print()
        break
    if data.strip()=="quit":
        break
    c.sendto(data.encode(),addr)
    print(c.recvfrom(1024)[0].decode())

c.close()