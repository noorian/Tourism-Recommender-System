# spot的信息都列举在此
# 将各基站加入离它最近的spot中
# 此处可改进。若一个基站离所有的spot都很远，可以将该基站剔除。具体代码请学长自行完成

import pickle as pk
from utils import *

with open('bs_id_loc_dict.pkl','rb') as f:
    bs_id_loc_dict = pk.load(f)    # (LAC:CID):(lng, lat)

spot_list = [

    Spot('株洲站',  113.1509277400, 27.8386530200,
         {'natural':True, 'human':False, 'museum':False}, 0*3600,
         {'spring': True, 'summer':True, 'autumn':True, 'winter': True}),

    Spot('株洲西站',  113.0627535700, 27.7940075400,
         {'natural':True, 'human':False, 'museum':False}, 0*3600,
         {'spring': True, 'summer':True, 'autumn':True, 'winter': True}),

    Spot('株洲南站',  113.1624070400, 27.7720062100,
         {'natural':True, 'human':False, 'museum':False}, 0*3600,
         {'spring': True, 'summer':True, 'autumn':True, 'winter': True}),

    Spot('株洲机场', 113.2047981100, 27.7703559800,
         {'natural': True, 'human': False, 'museum': False}, 0 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('神农谷',  114.0020062400, 26.5038025800,
         {'natural':True, 'human':False, 'museum':False}, 8*3600,
         {'spring': True, 'summer':True, 'autumn':True, 'winter': False}),

    Spot('湘江风光带', 113.1338949400, 27.8384002400,
         {'natural':True, 'human':False, 'museum':False}, 2*3600,
         {'spring': True, 'summer':False, 'autumn':True, 'winter': False}),

    Spot('神农城',  113.1265647488, 27.8293829091,
         {'natural':False, 'human':True, 'museum':False}, 2*3600,
         {'spring': True, 'summer':True, 'autumn':True, 'winter': True}),

    Spot('方特欢乐世界', 113.1856560500,  27.9928179500,
         {'natural':False, 'human':True, 'museum':False}, 8*3600,
         {'spring': True, 'summer':True, 'autumn':True, 'winter': True}),

    Spot('石峰公园',  113.1099932900, 27.8694225300,
         {'natural': False, 'human': True, 'museum': False}, 2*3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('神农公园', 113.1397392709, 27.8473154829,
         {'natural': False, 'human': True, 'museum': False}, 2*3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('云阳山', 113.4637093525, 26.7586304429,
         {'natural': True, 'human': True, 'museum': False}, 6*3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('酒埠江', 113.5590172090, 27.2199727833,
         {'natural': True, 'human': True, 'museum': False}, 8*3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': False}),

    Spot('炎帝陵', 113.6671209464, 26.4219628580,
         {'natural': False, 'human': True, 'museum': False}, 3 * 3600,
         {'spring': True, 'summer': False, 'autumn': True, 'winter': False}),

    Spot('大京',  113.2556768101, 27.8439457925,
         {'natural': True, 'human': True, 'museum': False}, 4 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('炎帝广场', 113.1166727843, 27.8235481080,
         {'natural': False, 'human': True, 'museum': False}, 1*3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('流芳园', 113.1329302420, 27.8281250861,
         {'natural': False, 'human': True, 'museum': False}, 1 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('城市规划展馆', 113.1289915488, 27.8310113091,
         {'natural': False, 'human': False, 'museum': True}, 2 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),


    Spot('湖南工业大学', 113.1212649132, 27.8208104525,
         {'natural': False, 'human': True, 'museum': False}, 1*3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('梨树洲', 113.9849567857, 26.3503158285,
         {'natural': True, 'human': False, 'museum': False}, 8*3600,
         {'spring': False, 'summer': True, 'autumn': False, 'winter': False}),


    Spot('空灵岸', 113.1032099132, 27.6632730799,
         {'natural': False, 'human': True, 'museum': False}, 2*3600,
         {'spring': False, 'summer': False, 'autumn': False, 'winter': True}),

    Spot('白龙洞', 113.7991220090, 27.2235708620,
         {'natural': True, 'human': True, 'museum': False}, 2*3600,
         {'spring': False, 'summer': False, 'autumn': True, 'winter': False}),

    Spot('云阳国家森林公园', 113.5077688273, 26.8004224055,
         {'natural': True, 'human': False, 'museum': False}, 2 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('婆仙岭', 113.2628884457, 27.8625141846,
         {'natural': True, 'human': True, 'museum': False}, 8 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('资福寺', 113.5254739206, 27.4758262851,
         {'natural': False, 'human': True, 'museum': False}, 2 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('株洲电视塔', 113.1138287843, 27.8217191080,
         {'natural': False, 'human': True, 'museum': False}, 1 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('皮佳洞仙境乐园',113.3395637083,  27.0034772644,
         {'natural': True, 'human': True, 'museum': False}, 2 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('仙庾古庙', 113.2534604457, 27.9373502728,
         {'natural': False, 'human': True, 'museum': False}, 1*3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('攸州公园', 113.3395353439, 27.0197779071,
         {'natural': False, 'human': True, 'museum': False}, 2 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('醴陵李立三故居', 113.5253478273, 27.6571425635,
         {'natural': False, 'human': True, 'museum': False}, 1 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('渌江书院',  113.5053670899, 27.6282873876,
         {'natural': False, 'human': True, 'museum': False}, 2*3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('仙人桥大峡谷', 113.6287582176, 27.2197854063,
         {'natural': True, 'human': False, 'museum': False}, 6 * 3600,
         {'spring': False, 'summer': True, 'autumn': False, 'winter': False}),


    Spot('炎陵湘山公园', 113.7617375734, 26.4893501152,
         {'natural': True, 'human': True, 'museum': False}, 4 * 3600,
         {'spring': True, 'summer': False, 'autumn': True, 'winter': False}),

    Spot('工农兵政府旧址', 113.5611162176, 26.7994328444,
         {'natural': False, 'human': True, 'museum': False}, 2 * 3600,
         {'spring': True, 'summer': True, 'autumn': True, 'winter': True}),

    Spot('炎陵湘山公园', 113.7617375734, 26.4893501152,
         {'natural': True, 'human': True, 'museum': False}, 4*3600,
         {'spring': True, 'summer': False, 'autumn': True, 'winter': False}),

]

spot_dict = {}
for spot in spot_list:
    spot_dict[(spot.lng, spot.lat)] = spot

bsNum = len(bs_id_loc_dict)   # the number of base stations
spotNum = len(spot_list)

bs_dict = {}    # (lng, lat) : base station
for i in bs_id_loc_dict:
    distance_list = []
    bs_lng, bs_lat = float(bs_id_loc_dict[i][0]), float(bs_id_loc_dict[i][1])
    for j in range(spotNum):
        spot_lng, spot_lat = spot_list[j].lng, spot_list[j].lat
        distance_list.append(get_distance(bs_lng, bs_lat, spot_lng, spot_lat))  # distance between base station and center
    distance_list[0] = distance_list[1] = distance_list[2] = distance_list[3] = 1000000
    min_distance = min(distance_list)
    spotIdx = distance_list.index(min_distance)
    bs = BS(bs_lng, bs_lat)
    bs.spot = (spot_list[spotIdx].lng, spot_list[spotIdx].lat)
    bs_dict[(bs_lng, bs_lat)] = bs
    spot_list[spotIdx].baseStation.append((bs_lng, bs_lat))
draw(spot_list)

for each in spot_list:
    print(len(each.baseStation))

with open('bs_dict.pkl','wb') as f:
    pk.dump(bs_dict, f)
with open('spot_dict.pkl','wb') as f:
    pk.dump(spot_dict, f)