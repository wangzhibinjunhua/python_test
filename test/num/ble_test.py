# -*- coding: utf-8 -*-
# @Time    : 2017-02-22 18:10
# @Author  : wzb<wangzhibin_x@foxmail.com>
import binascii
import struct
import sys
import unicodedata





data=[0x6a,0x75]

g_x=struct.unpack('<l',struct.pack('4B',*data))
print(g_x)


