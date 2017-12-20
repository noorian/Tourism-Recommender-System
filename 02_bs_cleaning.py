# 扒取基站经纬度坐标，并将其保存在字典中，字典中每一项的key为(LAC,CID)，value为(longitude, latitude)
# 扒取的网址为http://www.gpsspg.com/bs.htm，进行扒取需要调用api(每天的访问次数有限)
# 部分基站的经纬度坐标可能并未收录，在扒取的过程中我们将这部分基站数据剔除

import requests as rq
import pickle as pk
import os

api = [
    ('5756','F72095BEA6360EFBAA536CFBCC8B347B'),     # hezh@vip.com
    ('5761','F7A2B28FBF1388EE7228E3D52DBE6274'),     # zhangyuef2014@qq.com
    ('6137','322F9E19B012C7911798DF6987CB679A'),     # hezh_bupt@qq.com
    ('6154','7E9B8A329642F533288D7BF827AE3B82'),     # 568422445@qq.com
    ('6156','4A708F7B77737D8DE01AF4A179D08CDB'),     # wangyanqingchn@163.com
    ('6157','745522007633FD6F0CCE7817966461F9')      # hezihao568422445@bupt.edu.cn
]

with open('bs_id_set.pkl', 'rb') as f:
    bs_id_set = pk.load(f)

if os.path.exists('bs_id_state_dict.pkl'):
    with open('bs_id_state_dict.pkl') as f:
        bs_id_state_dict = pk.load(f)
else:
    bs_id_state_dict = {}
    for each in bs_id_set:
        bs_id_state_dict[each] = 'unprocessed'

if os.path.exists('bs_id_loc_dict.pkl'):
    with open('bs_id_loc_dict.pkl','rb') as f:
        bs_id_loc_dict = pk.load(f)
else:
    bs_id_loc_dict = {}

if os.path.exists('bs_id_js_dict.pkl'):
    with open('bs_id_js_dict.pkl','rb') as f:
        bs_id_js_dict = pk.load(f)
else:
    bs_id_js_dict = {}

api_idx = 0
log_no = 0
for each in bs_id_set:
    log_no += 1
    LAC, CI = each[0], each[1]
    if bs_id_state_dict[(LAC, CI)] == 'unprocessed':
        print('this is a new station')
        while (1):
            r = rq.get("http://api.gpsspg.com/bs/?oid=%s&key=%s&bs=460,01,%s,%s&output=json"
                       % (api[api_idx][0], api[api_idx][1], LAC, CI))
            js = r.json()
            print(js)
            if js['status'] == 200:
                if js['result'][0]['address'][0:6] != '湖南省株洲市':
                    break
                lng = js['result'][0]['lng']
                lat = js['result'][0]['lat']
                bs_id_loc_dict[(LAC, CI)] = (lng, lat)
                bs_id_js_dict[(LAC, CI)] = js
                print(len(bs_id_loc_dict))
                bs_id_state_dict[(LAC, CI)] = 'ok'
                break
            elif js['status'] == 404:
                bs_id_state_dict[(LAC, CI)] = 'not included'
                break
            elif js['status'] == 901:
                api_idx += 1
                if api_idx == len(api):
                    print('api runs out')
                    assert False
                continue
            else:
                break
    if len(bs_id_loc_dict) % 20 == 0 and len(bs_id_loc_dict) != 0:
        with open('bs_id_state_dict.pkl', 'wb') as f:
            pk.dump(bs_id_state_dict, f)
        with open('bs_id_lac_dict.pkl', 'wb') as f:
            pk.dump(bs_id_loc_dict, f)
        with open('bs_id_js_dict.pkl', 'wb') as f:
            pk.dump(bs_id_js_dict, f)
        print("successfully saved", len(bs_id_loc_dict))

with open('bs_id_state_dict.pkl', 'wb') as f:
    pk.dump(bs_id_state_dict, f)
with open('bs_id_loc_dict.pkl', 'wb') as f:
    pk.dump(bs_id_loc_dict, f)
with open('bs_id_js_dict.pkl', 'wb') as f:
    pk.dump(bs_id_js_dict, f)
print("successfully saved",  len(bs_id_loc_dict))
