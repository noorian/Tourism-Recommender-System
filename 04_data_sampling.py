# 数据放在path对应的目录下，解释和01中相同
# 这一步为数据采样，采样比为1:25，并只抽取出对用户行程推荐有帮助的列，其他列去掉
# 采样后的数据存放在工程目录下的data文件夹中
# 在时间充裕的情况下，可以不采样，充分利用所有数据，即设计采样比为1：1

sample_ratio = 25

import pickle as pk
import os,csv
from utils import *

with open('bs_id_loc_dict.pkl','rb') as f:
    bs_id_loc = pk.load(f)
with open('bs_dict.pkl', 'rb') as f:
    bs_dict = pk.load(f)
date = []
for i in range(301, 332):
    date.append('%04d' % i)
for i in range(401, 431):
     date.append('%04d' % i)
for i in range(501, 508):
    date.append('%04d' % i)
path = 'G:\data'
for each_date in date:
    fileName = 'SCOTT_GB_2013' + each_date + '.CSV'
    with open(os.path.join(path, fileName), encoding='utf-8') as file:
        f = csv.reader(file)
        log_no = 0
        content = ''
        for log in f:
            log_no += 1
            if log_no % sample_ratio == 0:
                if log_no % 10000 ==0:
                    print(each_date, log_no)
                LAC, CID, time, userID, data = log[1], log[2], log[3], log[4], log[-1]
                if (LAC, CID) in bs_id_loc and data != '' and float(data) != 0:
                    bs_lng, bs_lat = float(bs_id_loc[(LAC, CID)][0]),float(bs_id_loc[(LAC, CID)][1])
                    spot_lng, spot_lat = str(bs_dict[(bs_lng, bs_lat)].spot[0]), str(bs_dict[(bs_lng, bs_lat)].spot[1])
                    content += spot_lng + ',' + spot_lat + ',' + time + ',' + userID + ',' + data + '\n'
    content = content[0:-1]
    dst_path = '.\data'
    dst_file_name = each_date + '.txt'
    with open(os.path.join(dst_path, dst_file_name), 'w') as f:
        f.write(content)
