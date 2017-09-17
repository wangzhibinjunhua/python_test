# -*- coding: utf-8 -*-
# @Time    : 2017-02-22 18:10
# @Author  : wzb<wangzhibin_x@foxmail.com>
import binascii
import struct
f=open('result_wf06094.txt','rb')
#fr=f.read()

#v_hex=binascii.b2a_hex(fr)

#print(v_hex)
#v_str=binascii.a2b_hex(v_hex)
#print(v_str)
w_f_4 = open('xy_wf06094.txt', 'ab')

count=0
tk_flag=0
a_flag=0
g_flag=0
while True:
	f_hex=binascii.b2a_hex(f.read(4))

	print(f_hex)
	if(f_hex== b'7472616b'):
		print('trak')
		#w_f_4.write("\r\n".encode())
		a_x_b= (f.read(4))
		print(binascii.b2a_hex(a_x_b))
		a_x_h=struct.unpack('4B', a_x_b)
		print(a_x_h)
		a_x = struct.unpack('<f', struct.pack('4B', *a_x_h))[0]
		print(a_x)
		a_str_v=str(a_x).encode()
		w_f_4.write(a_str_v)
			#w_f_4.write(",".encode())
			#if(n==2):
			#	w_f_4.write("\r\n".encode())
			#else:
			#	w_f_4.write(",".encode())
		w_f_4.write(",".encode())
		a_y_b = (f.read(4))
		print(binascii.b2a_hex(a_y_b))
		a_y_h = struct.unpack('4B', a_y_b)
		print(a_y_h)
		a_y = struct.unpack('<f', struct.pack('4B', *a_y_h))[0]
		print(a_y)
		a_str_v = str(a_y).encode()
		w_f_4.write(a_str_v)

		w_f_4.write("\r\n".encode())
		count+=1
		continue
	else:
		if(f_hex==(b'')):break
		continue


f.close()
w_f_4.close()
