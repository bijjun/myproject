

from socket import *

IP = '127.0.0.1'
SERVER_PORT = 50000 #端口号
BUFLEN = 1024  #最大字节

# 实例化socket对象
dataSocket = socket(AF_INET, SOCK_STREAM)

# 连接服务端socket
dataSocket.connect((IP, SERVER_PORT))

while True:
    # 从终端读入用户输入的字符串
    toSend = input('>>> ')
    if  toSend =='exit':
        break

    dataSocket.send(toSend.encode())
    recved = dataSocket.recv(BUFLEN)
    # 如果返回空bytes，表示对方关闭了连接
    if not recved:
        break
    # 打印读取的信息
    print(recved.decode())

dataSocket.close()