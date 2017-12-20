# 这一步是计算每个spot的兴趣度，不需要做任何修改

import pickle as pk
import numpy as np

with open('spot_list.pkl', 'rb') as f:
    spot_list = pk.load(f)
spot_num = len(spot_list)

with open('user_data_mat.pkl','rb') as f:
    user_data_mat = pk.load(f)

I = np.ones((spot_num, 1))
Ip = np.zeros((spot_num, 1))
maxError = 1e-30

iteration = 0
while (np.sum(I - Ip)**2)**0.5 > maxError:
    Ip = I
    I = np.dot(np.dot(user_data_mat.T, user_data_mat), I)   # In+1 = mat.T * mat * In
    I = I / (sum(I**2)**0.5)
    iteration += 1
    print('this is the'+str(iteration)+'th iteration')

print('--------------------------')
print('the overall times of iteration is ', iteration)
for i in range(len(I)):
    print(I[i][0])
    spot_list[i].interest = I[i][0]
print('--------------------------')
print('--------------------------')
print('')
print('')

with open('spot_list.pkl', 'wb') as f:
    pk.dump(spot_list, f)