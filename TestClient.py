from Compressionserver import encodeimage,CompressionServer,Client
import cv2
import time
‘’‘’
def sendimage(client,imagename,id,qual,target,port):
    image = cv2.imread(imagename)
    image_id = int(id)
    qual = int(qual)
    port = int(port)
    client.adjustqual(qual)
    client.refreshimage(image,image_id)
    client.__send__(target,port)


if __name__ == '__main__':
    client1 = Client('127.0.0.1',8910,'user1')
    while True:
        qqual = input("输入需要的图片质量（1-100）: ")
        imagefilename = input("输入图片文件名:")
        image_id= input('请输入需要的图片id: ')
        addrtosend = input("请输入发送目标的ip地址:")
        porttosend = input("请输入发送目标的端口:")

        s = time.time()
        sendimage(client1,imagefilename,image_id,qqual,addrtosend,porttosend)
        print((time.time() - s) * 1000)
    '''
    while True:
        #测试的时候压缩质量qual设成手动输入，可以调，范围1-100
        qual = input("输入需要的图片质量（10-100）: ")
        client1.adjustqual(qual)
        image = cv2.imread('test.jpg')
        image_id=1
        client1.refreshimage(image,image_id)
        client1.__send__('192.168.1.6',8889)
    '''