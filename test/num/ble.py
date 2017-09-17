# -*- coding: utf-8 -*-
# @Time    : 2017-02-22 18:10
# @Author  : wzb<wangzhibin_x@foxmail.com>
import binascii
import struct
f=open('123.bin','rb')
#fr=f.read()

#v_hex=binascii.b2a_hex(fr)

#print(v_hex)
#v_str=binascii.a2b_hex(v_hex)
#print(v_str)
w_f_4 = open('44.txt', 'ab')
w_f_5 = open('55.txt', 'ab')
count=0
while True:
	f_hex=binascii.b2a_hex(f.read(2))
	print(f_hex)
	if(f_hex== b'6768'):
		print('gh')
		w_f_4.write("\r\n".encode())
		n=0
		while n<3:
			a_x_b= (f.read(4))
			print(binascii.b2a_hex(a_x_b))
			a_x_h=struct.unpack('4B', a_x_b)
			print(a_x_h)
			a_x = struct.unpack('<f', struct.pack('4B', *a_x_h))[0]
			print(a_x)
			a_str_v=str(a_x).encode()
			w_f_4.write(a_str_v)
			w_f_4.write(",".encode())
			n+=1

		#w_f.write(gh_v)
		count+=1
		continue
	elif(f_hex == b'7972'):
		print('yr')
		w_f_5.write("\r\n".encode())
		n = 0
		while n < 3:
			g_x_b = (f.read(4))
			print(binascii.b2a_hex(g_x_b))
			g_x_h = struct.unpack('4B', g_x_b)
			print(g_x_h)
			g_x = struct.unpack('<f', struct.pack('4B', *g_x_h))[0]
			print('gxyz=%s' % (g_x))
			g_str_v = str(g_x).encode()
			w_f_5.write(g_str_v)
			w_f_5.write(",".encode())
			n += 1
		continue
	else:
		if(f_hex==(b'')):break
		continue


f.close()
w_f_4.close()
w_f_5.close()