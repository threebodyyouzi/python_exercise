import socket

host=""    #服务监听在0.0.0.0上
port=12345 #服务监听的端口号,一般大于1024
addr=(host,port)
s=socket.socket()   #创建套接字,默认使用TCP
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)        #为套接字绑定地址
s.listen(1)         #自动监听过程,1表示允许多少个客户端等待
cli_sock,cli_addr=s.accept() #接收客户端连接,返回客户端套接字和地址
print("hello",cli_addr)
data=cli_sock.recv(1024)
print(data)
cli_sock.send(b"I C U\r\n")
cli_sock.close()
s.close()