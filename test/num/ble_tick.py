# -*- coding: utf-8 -*-
# @Time    : 2017-02-22 18:10
# @Author  : wzb<wangzhibin_x@foxmail.com>
import binascii
import struct

f = open('resultz.txt', 'rb')
# fr=f.read()

# v_hex=binascii.b2a_hex(fr)

# print(v_hex)
# v_str=binascii.a2b_hex(v_hex)
# print(v_str)
w_f_4 = open('tick0606.txt', 'ab')

count = 0
tk_flag = 0
a_flag = 0
g_flag = 0
while True:
    f_hex = binascii.b2a_hex(f.read(4))

    print(f_hex)
    if (f_hex == b'7472616b'):
        print('trak')
        # w_f_4.write("\r\n".encode())
        f.read(4)
        f.read(4)
        f.read(4)
        a_x_b = (f.read(4))
        print(binascii.b2a_hex(a_x_b))
        a_x_h = struct.unpack('4B', a_x_b)
        print(a_x_h)
        a_x = struct.unpack('<L', struct.pack('4B', *a_x_h))[0]
        print(a_x)
        a_str_v = str(a_x).encode()
        w_f_4.write(a_str_v)
        w_f_4.write(",".encode())
        a_x = a_x * 1.9 / 1000
        a_str_v = str(a_x).encode()
        w_f_4.write(a_str_v)

        w_f_4.write("\r\n".encode())

        continue
    else:
        if (f_hex == (b'')): break
        continue

f.close()
w_f_4.close()
