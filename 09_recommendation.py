import pickle as pk
import json
import copy

with open('spot_list.pkl', 'rb') as f:
    spot_list = pk.load(f)
with open('travel_mat.pkl', 'rb') as f:
    travel_mat = pk.load(f)

spot_name_id_dict = {}
spot_id_name_dict = {}
for i in range(len(spot_list)):
    spot_name_id_dict[spot_list[i].name] = i
    spot_id_name_dict[i] = spot_list[i].name

# 下面几项可以手动修改，注意spot_type中可以设置多项为true，表示一个用户可能喜欢多种景点，比如自然、人文、博物馆三种都喜欢
ori_spot = '株洲站'
dst_spot = '株洲机场'
hour = 14
minute = 0
season = 'autumn'   # spring, summer, autumn, winter
spot_type = {'natural': True, 'human': False, 'museum': False}     # natural spot, human spot, museum




t_max = hour*3600 + minute*60
ori_idx, dst_idx = spot_name_id_dict[ori_spot], spot_name_id_dict[dst_spot]

class Itinerary:
    def __init__(self, ori_idx, dst_idx, t_max, season, spot_type):
        self.t_max = t_max
        self.stay_list = [ori_idx, dst_idx]
        self.season = season
        self.spot_type = spot_type
        self.route = []
        self.travel_time_list = []
        self.t_stay_sum = 0
        self.t_travel_sum = 0
        self.t_sum = 0
        self.interest = 0
        self.score = 0
        self.description = {}

    def get_stay_time(self):
        self.t_stay_sum = 0
        for i in range(len(self.stay_list)-2):
            self.t_stay_sum += spot_list[self.stay_list[i+1]].duration

    def get_travel_time(self):
        self.travel_time_list = []
        self.t_travel_sum = 0
        for i in range(len(self.stay_list)-1):
            js = travel_mat[i][i+1]
            duration = js['result']['routes'][0]['duration']
            self.travel_time_list.append(duration)
            self.t_travel_sum += duration

    def get_interest(self):
        self.interest = 0
        for i in range(len(self.stay_list)-2):
            spot = spot_list[self.stay_list[i+1]]
            mismatch = 0
            if not spot.season[self.season]:
                mismatch += 1

            count = 0
            for each_type in self.spot_type:
                if self.spot_type[each_type] and spot_type[each_type]:
                    break
                else:
                    count += 1
            if count == 4:
                mismatch += 1

            interest = spot.interest * pow(0.9, mismatch)
            self.interest += interest**2
        self.interest **= 0.5

    def get_score(self):
        self.score = ((self.t_stay_sum/self.t_max)**2 + self.interest**2) ** 0.5

    def get_route(self):
        self.route = []
        subroute_num = len(self.stay_list) - 1
        for i in range(subroute_num):  # for every subroute in route
            js = travel_mat[i][i+1]
            path_num = len(js['result']['routes'][0]['steps'])
            subroute = []
            for j in range(path_num):  # for every path in subroute
                path = js['result']['routes'][0]['steps'][j]['path'].split(';')
                path1 = []
                for each in path:  # turn path into a list with float data
                    [lng, lat] = each.split(',')
                    path1.append([lng, lat])
                path = path1
                if j != 0 and j != path_num - 1:
                    del path[0]
                subroute.extend(path)
            if i != 0 and i != subroute_num - 1:
                del subroute[0]
            self.route.extend(subroute)

    def update(self):
        self.get_stay_time()
        self.get_travel_time()
        self.t_sum = self.t_stay_sum + self.t_travel_sum
        self.get_interest()
        self.get_score()
        self.get_route()

    def display(self):
        # print the path on the screen
        print('travel_route: ', end='')
        print(spot_id_name_dict[self.stay_list[0]], end='')
        for i in range(1, len(self.stay_list)):
            print('->', spot_id_name_dict[self.stay_list[i]], end = '')
        print('')
        print('spot interest:',end='')
        for i in range(len(self.stay_list)-2):
            print(spot_list[self.stay_list[i+1]].interest,' ',end='')
        print('')
        print('stay time: ', end='')
        for i in range(len(self.stay_list)-2):
            print(spot_list[self.stay_list[i+1]].duration, end=' ')
        print('')
        print('max time:', self.t_max, 's')
        print('stay time', self.t_stay_sum, 's')
        print('travel time', self.t_travel_sum, 's')
        print('stay time // max time', self.t_stay_sum / self.t_max)
        print('interest:', self.interest)
        print('score:', self.score / (2**0.5) * 100)

        # save the description of the path into a json file
        with open('route.json', 'w') as json_file:
            json_file.write(json.dumps(self.route))

        origin, destination = spot_list[self.stay_list[0]], spot_list[self.stay_list[-1]]
        ori_lng, ori_lat, ori_name = str(origin.lng), str(origin.lat), origin.name
        dst_lng, dst_lat, dst_name = str(destination.lng), str(destination.lat), destination.name
        self.description['origin'] = [ori_lng, ori_lat, ori_name]
        self.description['destination'] = [dst_lng, dst_lat, dst_name]
        self.description['waypoints'] = []
        self.description['path_time'] = []
        for i in range(len(self.stay_list)-1):
            waypoint = spot_list[self.stay_list[i+1]]
            self.description['waypoints'].append([str(waypoint.lng), str(waypoint.lat), waypoint.name, waypoint.duration])
            self.description['path_time'].append(str(self.travel_time_list[i]))
        self.description['duration'] = str(self.t_sum)
        self.description['staytime_ratio'] = str(self.t_stay_sum / self.t_max)
        self.description['interest'] = str(self.interest)
        self.description['score'] = str(self.score / (2**0.5) * 100)
        with open('itinerary.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(self.description, ensure_ascii=False))

def addSpot(itnry):
    best_itnry = copy.deepcopy(itnry)
    for e in range(len(itnry.stay_list)-1):
        for v in range(len(spot_list)):
            if v in itnry.stay_list or spot_list[v].interest == 0:
                continue
            else:
                new_itnry = copy.deepcopy(itnry)
                if itnry.t_sum < itnry.t_max:
                    new_itnry.stay_list.insert(e+1, v)
                    new_itnry.update()
                    if new_itnry.t_sum > itnry.t_max:
                        new_itnry.stay_list.pop(e + 1)
                        new_itnry.update()
                    if best_itnry.score < new_itnry.score:
                        best_itnry = new_itnry
    if best_itnry.score == itnry.score:
        return itnry
    else:
        rec = addSpot(best_itnry)
    return rec

itinerary = Itinerary(ori_idx, dst_idx, t_max, season, spot_type)
itinerary = addSpot(itinerary)
itinerary.display()