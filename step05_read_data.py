# 一条一条地读取记录
# 我们这里只读取了06:00之后、并且数据流量大于500的记录，其他记录舍弃
# 这两个参数可调。600代表06:00之后

import os
import pickle as pk
from utils import *

timeThreshold = 600
dataThreshold = 500
user_dict = {}

with open('spot_dict.pkl','rb') as f:
    spot_dict = pk.load(f)

path = '.\data'
date = []
for i in range(301, 332):
    date.append('%04d' % i)
for i in range(401, 431):
     date.append('%04d' % i)
for i in range(501, 508):
    date.append('%04d' % i)
for each_date in date:
    fileName = each_date + '.txt'
    with open(os.path.join(path, fileName)) as file:
        log_no = 0
        for line in file:
            if line[-1] == '\n':
                line = line[0:-1]
            line = line.split(',')
            log_no += 1
            if log_no % 1000 ==0:
                print(each_date, log_no)
            spot_lng, spot_lat, time, userID, data = line[0], line[1], line[2], line[3], line[4]

            if int(time[11: 13] + time[14: 16]) >= timeThreshold and float(data) >= dataThreshold:
                spot_lng = float(spot_lng)
                spot_lat = float(spot_lat)
                data = float(data)

                # update user list
                if userID not in user_dict:
                    user = User(userID)
                    user.addSpot(spot_lng, spot_lat, data)
                    user_dict[userID] = user
                else:
                    user_dict[userID].addSpot(spot_lng, spot_lat, data)

                # update base station list
                spot_dict[(spot_lng , spot_lat)].addUser(userID, data)

user_list = list(user_dict.values())
spot_list = list(spot_dict.values())

with open('user_dict.pkl', 'wb') as f:
    pk.dump(user_dict, f)
with open('spot_dict.pkl', 'wb') as f:
    pk.dump(spot_dict, f)
with open('user_list.pkl', 'wb') as f:
    pk.dump(user_list, f)
with open('spot_list.pkl', 'wb') as f:
    pk.dump(spot_list, f)
