import socket

# Here we are creating socket in our computer which is ready to connect but not yet connected
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # Here socket is connecting to that host at port 80

# After connection is made we have to send get request with protocol HTTP1.0
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# encode() converts inside python unicode format to UTF8
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    # we will receive upto 512 characters at a time
    if (len(data) < 1):
        break
    print(data.decode()) # received data will be in UTF8 format which we will be converting to unicode using decode()
mysock.close()

