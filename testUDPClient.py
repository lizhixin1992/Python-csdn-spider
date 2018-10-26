# coding:utf-8

from socket import *


HOST = "127.0.0.1"
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpClient = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("输入信息：")
    if not data:
        break
    udpClient.sendto(bytes(data,'utf-8'), ADDR)
    data,addr = udpClient.recvfrom(BUFSIZE)
    if not data:
        break
    print("接收到的数据：%s" % str(data,"utf-8"))
    print("服务器地址：", addr)

udpClient.close()