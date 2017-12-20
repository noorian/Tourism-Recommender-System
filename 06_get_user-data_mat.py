# 这一步是得到用户-访问数据量矩阵，不需要做任何更改

import pickle as pk
import numpy as np

with open('user_list.pkl','rb') as f:
    user_list = pk.load(f)

with open('spot_list.pkl','rb') as f:
    spot_list = pk.load(f)

userNum = len(user_list)
centerNum = len(spot_list)

user_data_mat = np.zeros((userNum, centerNum))   # initialize the matrix
for i in range(userNum):
    for j in range(centerNum):
        print(i, j)
        if (spot_list[j].lng, spot_list[j].lat) in user_list[i].spotData:
            user_data_mat[i][j] = user_list[i].spotData[(spot_list[j].lng, spot_list[j].lat)]

with open('user_data_mat.pkl', 'wb') as f:
    pk.dump(user_data_mat, f)