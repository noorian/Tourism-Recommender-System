# *************将所有的基站LAC和CID提取出来保存在集合里*************
# 使用方法：将数据放在path对应的目录下，应该为SCOTT_GB_20130301.csv到SCOTT_GB_20130507.csv共68个csv文件
# 如果只有部分文件，那么应修改生成date列表的部分代码。
# 数据请找周裕杰要
# 如果想依次运行完01至09，请事先将工程目录下所有的.pkl文件删除


import os, csv, pickle as pk

bs_id_set = set()

path = 'G:\data'
date = []
for i in range(301, 332):
    date.append('%04d' % i)
for i in range(401, 431):
     date.append('%04d' % i)
for i in range(501, 508):
    date.append('%04d' % i)


for each_date in date:
    file_name = 'SCOTT_GB_2013' + each_date + '.CSV'
    with open(os.path.join(path, file_name), encoding='utf-8') as file:
        f = csv.reader(file)
        log_no = 0
        for line in f:
            log_no += 1
            if log_no % 10000 == 0:
                print('*********', each_date, '****', '%08d' % log_no, '*******', len(bs_id_set))
            LAC, CI = line[1], line[2]
            bs_id_set.add((LAC,CI))

with open('bs_id_set.pkl', 'wb') as f:
    pk.dump(bs_id_set, f)
print(len(bs_id_set))