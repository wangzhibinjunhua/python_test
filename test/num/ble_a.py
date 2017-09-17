# -*- coding: utf-8 -*-
# @Time    : 2017-02-22 18:10
# @Author  : wzb<wangzhibin_x@foxmail.com>
import binascii
import struct
f=open('ble_test-0316.txt','rb')
#fr=f.read()

#v_hex=binascii.b2a_hex(fr)

#print(v_hex)
#v_str=binascii.a2b_hex(v_hex)
#print(v_str)
w_f_4 = open('a_wbin0316.txt', 'ab')

count=0
tk_flag=0
while True:
	f_hex=binascii.b2a_hex(f.read(2))

	print(f_hex)
	if(f_hex == b'746b'):
		t_b=f.read(4)
		t_b_h=struct.unpack('4B', t_b)
		t_v=struct.unpack('<L', struct.pack('4B', *t_b_h))[0]
		t_v_str=str(t_v).encode()
		w_f_4.write(t_v_str)
		w_f_4.write(",".encode())
		tk_flag=1
		continue
	elif(f_hex== b'6768'):
		print('gh')
		#w_f_4.write("\r\n".encode())
		n=0
		if(tk_flag==0):
			w_f_4.write("0,".encode())
		while n<3:
			a_x_b= (f.read(4))
			print(binascii.b2a_hex(a_x_b))
			a_x_h=struct.unpack('4B', a_x_b)
			print(a_x_h)
			a_x = struct.unpack('<f', struct.pack('4B', *a_x_h))[0]
			print(a_x)
			a_str_v=str(a_x).encode()
			w_f_4.write(a_str_v)
			#w_f_4.write(",".encode())
			if(n==2):
				w_f_4.write("\r\n".encode())
			else:
				w_f_4.write(",".encode())
			n+=1

		#w_f.write(gh_v)
		tk_flag=0
		count+=1
		continue
	else:
		if(f_hex==(b'')):break
		continue


f.close()
w_f_4.close()
