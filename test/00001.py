# -*- coding: utf-8 -*-
# @Time    : 2016-11-17 10:15
# @Author  : wzb<wangzhibin_x@foxmail.com>
import random

def create_num(num,long):
	str = 'qwertyuiopasdfghjklzxcvbnm1234567890'
	b = []
	for i in range(num):
		a = ''
		for j in range(long):
			a+=random.choice(str)

		b.append(a)
	for i in range(len(b)):
		print(b[i])

	return b

if __name__ == '__main__':
	create_num(10,10)
