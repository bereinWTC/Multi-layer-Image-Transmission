import os
from socket import *
import sys
from time import ctime
import threading
import json
import time
import numpy as np
import cv2
import struct

def encodeimage(img,qual):
    #s=time.time()
    tmp = cv2.imencode('.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY), qual])
    #print((time.time()-s)*1000)
    #print(qual)
    return tmp

class CompressionServer:  # server收到用户的需求并执行，我这里写的是用户发给server需要的质量，server将对应画质图像发回给用户
    #server每次收到客户指令的时候，要send给所有的friends，让他们执行同样的指令——所有friend server的tree应该是保持一致的
    #理论讲server可以多个并用，这里没把这部分加进来。先用一个
    def __init__(self, addr, portno, user='User1'):
        self.port = portno
        self.addr = addr
        self.friends = []
        self.clients = []
        self.user = user
        self.image = cv2.imread('test.jpg')


    def bind_socket(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((self.addr, self.port))
        self.sock.listen(12)

    def refreshimage(self,img):
        #更新当前需要发送的帧。这里暂时用了一个imread代替
        self.image = img

    def receive(self):  # 收到需求，编码图片，发回去

        while True:
            #先绑端口
            conn_socket, addr = self.sock.accept()
            print("Connect from : ", addr)
            #print('here')

            header = conn_socket.recv(4)
            size = struct.unpack("i", header)
            print("size is: ", size[0])
            img_rawdata = b""

            img_rawdata += conn_socket.recv(size[0])
            if not img_rawdata:
                continue
            img_rawdata = json.loads(img_rawdata)
            img_list = img_rawdata['img']
            img_array = np.array(img_list, dtype='uint8')

            print(img_rawdata['id'],img_rawdata['qual'],size)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # cv2.imshow('target',img)
            imgfilename = str(img_rawdata['id'])+'qual'+str(img_rawdata['qual'])+'.jpg'
            cv2.imwrite(imgfilename, img)



    def run(self):
        # host = self.addr
        # port = self.port
        # s.bind((host, port))

        while True:
            print("Listening....")
            # self.connection.append(conn_socket)
            self.receive()
            # leader_server_thread = threading.Thread(target=self.receive(self.sock), args=(conn_socket))
            # leader_server_thread = threading.Thread(target=self.receive())
            # leader_server_thread.setDaemon(True)
            # leader_server_thread.start()
            # print("active threads:")
            # print(threading.active_count())

class Client: #Client做两件事情，向server发送一个qual以获取图片，以及输出获取的图片
    def __init__(self, addr, portno,name):
        self.port = portno
        self.sock = socket(AF_INET,SOCK_STREAM)
        self.addr = addr
        self.name = name
        self.servers = []
        self.qual = 100
    def refreshimage(self,img,id):
        self.image = img
        self.imageid = id
    def adjustqual(self,aqual):
        self.qual=aqual

    def __send__(self, addr, port):
        #print("Start to connect with server")
        self.sock = socket(AF_INET,SOCK_STREAM)
        self.sock.connect((addr,port))
        imgtosend = encodeimage(self.image,self.qual)
        image_id = self.imageid

        img_rawdata = imgtosend[1].tolist()
        print(sys.getsizeof(img_rawdata))
        datatosend = json.dumps({'id':image_id,'qual': self.qual, 'img': img_rawdata})
        size = sys.getsizeof(datatosend)
        print("sending image id ",self.imageid,"of data size:", size," with qual", self.qual)
        header = struct.pack("i", size)
        self.sock.sendall(header)
        self.sock.sendall(datatosend.encode())



    def getsocketfd(self):
        return self.sock