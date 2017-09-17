# -*- coding: utf-8 -*-
# @Time    : 2017-02-25 9:00
# @Author  : wzb<wangzhibin_x@foxmail.com>

import numpy as np
import pandas as pd


txt=np.loadtxt(open("ao_0410_01_3.txt","rb"),delimiter=",",skiprows=1)
txt_df=pd.DataFrame(txt)
txt_df.to_csv('ao_0410_01_3.csv',index=False)



