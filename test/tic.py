# -*- coding: utf-8 -*-
# @Time    : 2016-12-23 17:10
# @Author  : wzb<wangzhibin_x@foxmail.com>



from urllib import request
with request.urlopen("http://huayinghealth.com") as f:
	data=f.read()
	for k,v in f.getheaders():
		print("%s:%s" % (k,v))

	print('Data',data.decode('utf-8'))
