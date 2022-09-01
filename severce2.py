from socket import *
from threading import Thread
from  time import sleep


IP = '127.0.0.1' #表示本机地址测试用
# 端口号
PORT = 50000
# 定义一次从socket缓冲区最多读入512个字节数据
BUFLEN = 512

listenSocket = socket(AF_INET, SOCK_STREAM) #实例化socket类

# socket绑定地址和端口
listenSocket.bind((IP, PORT))


# 使socket处于监听状态，等待客户端的连接请求 最多8个连接
listenSocket.listen(8)
print(f'服务端启动成功，在{PORT}端口等待客户端连接...')

def listenData(dataSocket,addr):#新线程入口函数
    while True:
        recved = dataSocket.recv(BUFLEN)  # 程序处于阻塞状态若无信息则继续等待
        #对方关闭连接则退出循环
        if not recved:
            break
        # 对收到的信息解码
        info = recved.decode()
        print(f'收到{addr}对方信息： {info}')
        # 对要发送的信息进行编码
        dataSocket.send(f'服务端接收到了信息 {info}'.encode())

    # 关闭dataSocket对象
    dataSocket.close()
    #listenSocket.close()

# dataSocket, addr = listenSocket.accept()#等待客户端进行链接,并创建新的dataSocket用于接收数据
# if(addr is not exit())
# print('接受一个客户端连接:', addr)

while True:
    dataSocket, addr = listenSocket.accept()  # 等待客户端进行链接,并创建新的dataSocket用于接收数据
    thread = Thread(target=listenData,
                    args=(dataSocket,addr)  # 入口函数参数
                    )
    thread.start()  # 创建新线程，执行入口函数代码


# #创建线程对象
# thread=Thread(target=listenData,
#               args=(dataSocket[0])#入口函数参数
#               )
