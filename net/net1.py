import socket
import struct
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
h="127.0.0.1"
p=2998
s.connect((h,p))
data = s.recv(4)
print data
strdata = struct.unpack("I", data)[0]
print strdata
s.send(str(strdata))
print s.recv(1024)
