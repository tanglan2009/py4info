import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(5120)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

mysock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock2.connect(('www.pythonlearn.com', 80))
mysock2.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock2.recv(5120)
    if (len(data) < 1):
        break
    print data;

mysock2.close()


