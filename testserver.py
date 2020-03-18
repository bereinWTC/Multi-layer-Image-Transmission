from Compressionserver import encodeimage,CompressionServer,Client

if __name__ == '__main__':
    Myserver = CompressionServer('192.168.1.6', 8889, user='user1')
    Myserver.bind_socket()
    Myserver.run()