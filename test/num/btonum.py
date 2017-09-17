# -*- coding: utf-8 -*-
# @Time    : 2017-02-28 9:52
# @Author  : wzb<wangzhibin_x@foxmail.com>
import struct
data=[]
data.append(0x00)
data.append(0x00)
data.append(0x00)
data.append(0x00)
num=struct.unpack('<l',struct.pack('4B',*data))
print(num)
data=[0x35,0x01,0x00,0x08]
num=struct.unpack('<l',struct.pack('4B',*data))
print(num)
data=[0x00,0x01,0x00,0x00]
num=struct.unpack('<L',struct.pack('4B',*data))[0]
print(num)