import json,decimal
from hiv.models import People,Place,Time

names=locals()
# 将时间转换为json
# class ComplexEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.time):
#             return int(obj.strftime('%H'))
#         elif isinstance(obj, decimal.Decimal):
#             return str(obj)
#         else:
#             return json.JSONEncoder.default(self, obj)

class DecimalJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)


# 获取地点-时间json
def place_time(place_names):
    genenral = []

    for place in place_names:
        place_all=place_lonlat(place)
        names['%s_people' % place] = People.objects.filter(place__place_name=place)
        count=0
        peoples=[]

        for people in names['%s_people' % place]:
            count=count+1
            person={}
            person["id"]=count
            person["name"] = people.name
            person["time"]={}
            day=1

            while day<=7:
                a = Time.objects.filter(people__name=people.name).filter(day_in_week=day).values_list('time',flat=True)
                person["time"][day]=list(a)
                day=day+1
            peoples.append(person)

        place_all["people"]=peoples
        genenral.append(place_all)
    places_time_json = json.dumps(genenral, cls=DecimalJSONEncoder)
    return places_time_json

# 获取地点-坐标
def place_lonlat(place):
    places_lonlat={}
    count=0
    count=count+1
    pl = Place.objects.get(place_name=place)
    lonlat={"x":pl.longtitude,"y":pl.latitude}
    places_lonlat["id"] = count
    places_lonlat["name"] = place
    places_lonlat["coords"] = lonlat
    # 地点-时间json
    # places_lonlat_json = json.dumps(places_lonlat,cls=DecimalJSONEncoder)
    return places_lonlat