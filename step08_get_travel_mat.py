# 事先保存每两个spot之间的行程信息矩阵，包括两点之间的路线、行驶耗时等。
# 实际的运用过程中是不需要这一步的，因为两点之间的形成信息需要实时获取，
# 但由于我们自己做的时候没钱买api的无限量访问，所以就事先把每两点之间的行程信息暂存下来。
# 此处我们选择的出行方式是开车driving，也可以选用其他方式。在URL中将mode更改为其他方式，
# driving（驾车）、walking（步行）、transit（公交）、riding（骑行）
# 更多出行方式请查阅百度地图API http://lbsyun.baidu.com/index.php?title=webapi/direction-api



import pickle as pk
import requests as rq
import os

with open('spot_list.pkl', 'rb') as f:
    spot_list = pk.load(f)
spot_num = len(spot_list)

if os.path.exists('travel_mat.pkl'):
    f = open('travel_mat.pkl', 'rb')
    travel_mat = pk.load(f)
else:
    travel_mat = [[0] * spot_num] * spot_num

ak = [
    "jnvU9LrC98VKS9oBrGgfKkGzFGCK3TPo",
    "pOeGxlQG4TXQ9QXoeWOoILsUgfCOGkGq",
    "GVbSTEgzFooVjLVqfmzTrGRO1fGhWPVG",
    "DD279b2a90afdf0ae7a3796787a0742e",
    "rPcvt9NrfXgmaAnAEl6Z3SU6GxV44R9E",
    "eOuWRKBKfyNnyw25T3MewMuzNGMHoWT5",
    "uO8VnNvG7UltHE6mYX1hhsqlN76O3c2p",
    "br91jy3hwYTkgQPrHy08GgPKLHwGeiah"
    "qxGvOaAdtZyLWFDsjdGbZaLXpkM3USvq",
    "w9ZbjLuIczNYtACFwe87moYn2NCbQz3r",
    "QLrlR5H6irsRqF44dt1WX3vDV8zSCVsg"
]
ak_num = len(ak)

ak_idx = 0
count = 0
for i in range(spot_num):
    for j in range(spot_num):
        if i == j:
            continue
        if travel_mat[i][j] == 0:
            ori_lng, ori_lat = str(round(spot_list[i].lng, 6)), str(round(spot_list[i].lat, 6))
            dst_lng, dst_lat = str(round(spot_list[j].lng, 6)), str(round(spot_list[j].lat, 6))
            while (1):
                url = "http://api.map.baidu.com/direction/v1?mode=driving" \
                      "&origin=%s,%s&destination=%s,%s&origin_region=株洲&destination_region=株洲" \
                      "&output=json&coord_type=wgs84&ak=%s" \
                      % (ori_lat, ori_lng, dst_lat, dst_lng, ak[ak_idx])
                r = rq.get(url)
                js = r.json()
                print(js)
                status = js['status']
                if status == 0:
                    print(spot_list[i].name, spot_list[j].name)
                    travel_mat[i][j] = js
                    break
                elif status == 302:
                    print('current ak runs out')
                    ak_idx += 1
                    if ak_idx == ak_num:
                        print('ak runs out')
                        assert False
                    continue
                else:
                    break

with open('travel_mat.pkl', 'wb') as f:
    pk.dump(travel_mat, f)