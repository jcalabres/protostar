import socket  
import struct

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("192.168.81.132", 2997))

sum=0  
for i in range(4):  
            n=s.recv(4)
            num=int(struct.unpack("<I", n)[0])
            print("[+]Num:"+str(num))
            sum+=num
print("[+]Result:"+str(sum))
result=struct.pack("<I",sum)
s.send(result)
print(s.recv(1024))  
s.close()  
