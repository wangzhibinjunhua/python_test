# -*- coding: utf-8 -*-
# @Time    : 2016-09-20 11:08
# @Author  : wzb<wangzhibin_x@foxmail.com>
# from PIL import Image, ImageDraw, ImageFont
#
# def add_num(img):
#     draw = ImageDraw.Draw(img)
#     myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
#     fillcolor = "#ff0000"
#     width, height = img.size
#     draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
#     img.save('result.jpg','jpeg')
#
#     return 0
# if __name__ == '__main__':
#     image = Image.open('test.png')
#     add_num(image)
# from collections import Counter
# import re
#
#
# def creat_list(filename):
#     datalist = []
#     with open(filename, 'r') as f:
#         for line in f:
#             content = re.sub("\"|,|\.", "", line)
#             datalist.extend(content.strip().split(' '))
#     return datalist
#
#
# def wc(filename):
#     print (Counter(creat_list(filename)))
#
# if __name__ == "__main__":
#     filename = 'test.txt'
#     wc(filename)
import numpy as np
import matplotlib.pyplot as mpl
import time
from scipy import optimize
start=time.clock()
c=np.array([1,1,1])
a=np.array([[3.05,4.0,6.15]])
b=np.array([7.9])

res=optimize.linprog(c,-a,b)
end=time.clock()
print(res.x)
print(end-start)



