import cv2

def encodeimage(img,qual):
    #s=time.time()
    tmp = cv2.imencode('.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY), qual])
    #print((time.time()-s)*1000)
    #print(qual)
    return tmp

image = cv2.imread('test.jpg')
#print(image)
while True:
    qq=input("ahahaha:")
    qq=int(qq)
    img_compressed = cv2.imencode('.jpg',image,[int(cv2.IMWRITE_JPEG_QUALITY), qq])
    print(img_compressed[1])
    print(img_compressed[1].shape)
    img_compressed=cv2.imdecode(img_compressed[1], cv2.IMREAD_COLOR)

    cv2.imwrite('test1.jpg',image)
    cv2.imwrite('test2.jpg',img_compressed)