import matplotlib.pyplot as plt
import numpy as np
import json
import copy
import cmath

class User:
    def __init__(self, id):
        self.id = id    # user's ID
        self.spotData = {}   # data through the spot    (spot_lng, spot_lat): data

    def addSpot(self, lng, lat, data):
        if (lng,lat) not in self.spotData:
            self.spotData[(lng, lat)] = data
        else:
            self.spotData[(lng, lat)] += data


class BS:
    def __init__(self, lng, lat):
        self.lng = lng
        self.lat = lat
        self.spot = (0,0)


class Spot:
    def __init__(self, name, lng, lat, _type, duration, season):
        self.name = name
        self.lng = lng
        self.lat = lat
        self.type = _type    # natural, human, museum
        self.duration = duration   # recommended visiting time
        self.season = season    # recommended visiting season
        self.interest = 0  # the interest of the center
        self.visitNum = 0
        self.data = 0
        self.baseStation = []   # (bs_lng, bs_lat)
        self.userData = {}  # userID: data

    def addUser(self, userID, data):
        self.visitNum += 1
        self.data += data
        if userID not in self.userData:
            self.userData[userID] = data
        else:
            self.userData[userID] += data


# def split(bigCenter):
#     """"split a big center into two small centers"""
#     lng = [_bs.lng for _bs in bigCenter.baseStation]
#     lat = [_bs.lat for _bs in bigCenter.baseStation]
#     min_lng, max_lng = min(lng), max(lng)
#     min_lat, max_lat = min(lat), max(lat)
#     smallCenter1 = Center(0,0)
#     smallCenter2 = Center(0,0)
#     if max_lng - min_lng >= max_lat - min_lat:     # span of longitude is greater that of latitude
#         mid_lng = (max_lng + min_lng) / 2
#         for _bs in bigCenter.baseStation:
#             if _bs.lng > mid_lng:
#                 smallCenter1.addBS(_bs)
#             else:
#                 smallCenter2.addBS(_bs)
#     else:                                           # span of latitude is greater thant that of longitude
#         mid_lat = (max_lat + min_lat) / 2
#         for _bs in bigCenter.baseStation:
#             if _bs.lat > mid_lat:
#                 smallCenter1.addBS(_bs)
#             else:
#                 smallCenter2.addBS(_bs)
#
#     smallCenter1.updateLoc()
#     smallCenter2.updateLoc()
#     return [smallCenter1, smallCenter2]


def draw(center_list):
    X = []
    Y = []
    color = []
    size = []
    for _center in center_list:
        X.append(_center.lng)
        Y.append(_center.lat)
        size.append(30)
        color_center = [0, 0, 0, 1]
        color_bs = [np.random.random(), np.random.random(), np.random.random(), 1]
        color.append(color_center)
        for _bs in _center.baseStation:
            X.append(_bs[0])
            Y.append(_bs[1])
            size.append(10)
            color.append(color_bs)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('Scatter Plot')   # 设置标题
    plt.xlabel('longitude')     # 设置X轴标签
    plt.ylabel('latitude') # 设置Y轴标签
    ax1.scatter(X, Y, c=color, marker='.',s=size)       # 画散点图
    plt.savefig("clustering.png")
    plt.show()  # 显示所画的图

def get_distance(lngA, latA, lngB, latB):
    """calculate the distance between two points according to their longitudes and latitudes"""
    # mlonA = lngA * cmath.pi / 180
    # mlatA = (90 - latA) * cmath.pi / 180
    # mlonB = lngB * cmath.pi / 180
    # mlatB = (90 - latB) * cmath.pi / 180
    # C = cmath.cos(mlatA) * cmath.sin(mlatB) * cmath.cos(mlonA - mlonB) + cmath.cos(mlatA) * cmath.cos(mlatB)
    # distance = 6371.004 * cmath.acos(C) * cmath.pi / 180
    dA = (lngA - lngB) **2
    dB = (latA - latB) **2

    return (dA + dB)**0.5

