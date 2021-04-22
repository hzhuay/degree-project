from flask import Flask, request
from server.config import Config
from server import app, db
from flask_cors import cross_origin
import pandas as pd
import json
#from config import dic_street
from sqlalchemy import func, or_, and_
from server.models import House
import joblib
import time
# from fuzzywuzzy import process, fuzz




# df = pd.read_csv('des2.csv')
# df.rename(columns={'名称':'name','总价':'totalPrice','面积':'area','小区名':'community'}, inplace=True)

# @app.route('/', methods=['GET','POST'])
# def index():
#     return 'Hello World'

# addr_set = set(df['community'].to_list())
# lst = list(addr_set)
dic = {}
directions = ['north','south','east','west','northeast','southeast','northwest','southwest']
order = ['area', 'floor', 'structure', 'decoration', 'elevatorRate', 'heating', 'elevator', 'block_price', 'block_fee', 'school', 'mall', 'traffic', 'medicine', 'south', 'north', 'east', 'west', 'southeast', 'southwest', 'northeast', 'northwest', 'totalFloor', 'year', 'district', 'street', 'ring', 'room', 'parlor', 'kitchen', 'bathroom']
model = joblib.load('server\\XGB_reg.dat')

# @app.route('/search_community', methods=['GET'])
# def search_community():
#     name = request.args.get("name", type=str)
#     return json.dumps(process.extract(name, addr_set, limit=10))

@app.route('/all', methods=['GET'])
# @cross_origin()
def all():
    return json.dumps(lst, ensure_ascii=False)


@app.route('/write', methods=['GET'])
# @cross_origin()
def write():
    index = request.args.get("index", type=str)
    name = request.args.get("name", type=str)
    address = request.args.get("address", type=str)
    dic[index] = {'name':name, 'address':address}
    return 'Hello World'

@app.route('/write_dict', methods=['GET'])
# @cross_origin()
def write_csv():
    with open('trans.txt', 'w', encoding="utf-8") as f:
        f.write(str(dic))
    return "wrtie over"

@app.route('/predict', methods=['POST'])
# @cross_origin()
def predict():
    
    dic = request.json

    print(dic)
    for item in directions:
        if item in dic['directions']:
            dic[item] = 1
        else:
            dic[item] = 0
    dic.pop('directions')
    if dic['elevator'] == True:
        dic['elevator'] = 1
    elif dic['elevator'] == False:
        dic['elevator'] = 0

    dic['street'] = dic_street['北工大']
    #模糊匹配 block_price, block_fee, year
    dic['block_price'] = 100000
    dic['block_fee'] = 2
    dic['year'] = 20
    df_predict = pd.DataFrame(dic,index=[0])
    print(df_predict.columns)
    print(df_predict.info())
    df_predict = df_predict[order]
    return str(model.predict(df_predict))

@app.route('/getHouses', methods=['POST', 'GET'])
# @cross_origin()
def get_houses():
    # tmp = df.loc[0:5,['name','totalPrice','area','community','location']].to_dict(orient='index')
    # return json.dumps([tmp[i] for i in tmp], ensure_ascii=False)
    page = request.args.get("page", type=int)
    offset = request.args.get("offset", type=int)
    min_price = request.args.get("minPrice", type=int)
    max_price = request.args.get("maxPrice", type=int)
    min_area = request.args.get("minArea", type=int)
    max_area = request.args.get("maxArea", type=int)
    district = request.args.get("district", type=str)
    block = request.args.get("block", type=str)
    sort_by = request.args.get("sortBy", type=int)
    sort_rule = request.args.get("sortRule", type=int)
    print(f"{min_price} {max_price}")
    print(f"{min_area} {max_area}")
    res = {}
    # res['total'] = db.session.query(func.count(House.id)).scalar()
    # start, end = (page-1) * offset, page * offset - 1

    # 根据条件筛选
    # price_rule = (lambda x: min_price < x < max_price) if max_price != 20 else (lambda x: min_price < x)
    # house_temp = db.session.query(House)
    # if max_price != 20:
    #     house_price = ( db.session.query(House.id).filter(House.total_price > min_price, House.total_price < max_price) )
    # else:
    #     house_price = ( db.session.query(House.id).filter(House.total_price > min_price) )
    
    # if max_area != 200:
    #     house_area = ( db.session.query(House.id).filter(House.area > min_area, House.area < max_area).filter(House.id.in_(house_price)) )
    # else:
    #     house_area = ( db.session.query(House.id).filter(House.area > min_area).filter(House.id.in_(house_price)) )
    # if district:
    #     house_district = ( db.session.query(House.id).filter(House.district == district).filter(House.id.in_(house_area)) )
    # else:
    #     house_district = house_area    
    # if block:
    #     house_block = ( db.session.query(House.id).filter(House.block == block).filter(House.id.in_(house_district)) )
    # else:
    #     house_block = house_district




    # if max_price != 20:
    #     house_price = ( db.session.query(House.id).filter(House.total_price > min_price, House.total_price < max_price) )
    # else:
    #     house_price = ( db.session.query(House.id).filter(House.total_price > min_price) )
    
    # if max_area != 200:
    #     house_area = ( db.session.query(House.id).filter(House.area > min_area, House.area < max_area).filter(House.id.in_(house_price)) )
    # else:
    #     house_area = ( db.session.query(House.id).filter(House.area > min_area).filter(House.id.in_(house_price)) )
    # if district:
    #     house_district = ( db.session.query(House.id).filter(House.district == district).filter(House.id.in_(house_area)) )
    # else:
    #     house_district = house_area    
    # if block:
    #     house_block = ( db.session.query(House.id).filter(House.block == block).filter(House.id.in_(house_district)) )
    # else:
    #     house_block = house_district    

    # 根据条件筛选
    start_time = time.process_time()
    tmp = House.query.filter(House.total_price > min_price, House.area > min_area)

    if max_price != 20:
        tmp = tmp.filter(House.total_price < max_price)

    if max_price != 200:
        tmp = tmp.filter(House.area < max_area)

    if district:
        tmp = tmp.filter(House.district == district)

    if block:
        tmp = tmp.filter(House.block == block)
    
    # 筛选到符合条件的房子的数量
    res['total'] = tmp.count()

    # 排序
    if sort_by == 1:
        tmp = tmp.order_by(House.total_price if sort_rule == 0 else House.total_price.desc())
    elif sort_by == 2:
        tmp = tmp.order_by(House.id if sort_rule == 0 else House.id.desc())

    # 分页
    houses = tmp.limit(offset).offset((page-1)*offset).all()
    
    # houses = db.session.query(House.title,House.total_price,House.area,House.location,House.name,House.block,House.des,House.avg_price).filter(House.id.in_(house_block)).all()
    
    # print(res['total'])
    # label = ['title','total_price','area','location','name','block','des','avg_price']
    # houses = [dict(zip(label,n)) for n in houses]
    # res['data'] = dict(zip(range(0,end-start+1),houses[start:end+1]))#问一下

    res['data'] = [h.to_dict() for h in houses]
    res['cnt'] = len(res['data'])
    # print(res['data'])


    # res = {}
    # res['total'] = len(df)
    # start, end = (page-1) * offset, page * offset - 1

    # # 根据条件筛选
    # price_rule = (lambda x: min_price < x < max_price) if max_price != 20 else (lambda x: min_price < x)
    # area_rule = (lambda x: min_area < x < max_area) if max_area != 200 else (lambda x: min_area < x)
    # tmp = df[df['total_price'].apply(price_rule)]
    # tmp = tmp[tmp['area'].apply(area_rule)]
    # if district:
    #     tmp = tmp[tmp['district'] == district]
    # if block:
    #     tmp = tmp[tmp['block'] == block]

    # # 排序
    # if sort_by == 1:
    #     tmp.sort_values(by="total_price", ascending=[False,True][sort_rule], inplace=True)

    # res['total'] = len(tmp)
    # res['data'] = tmp.reset_index(drop=True).loc[start:end,['title','total_price','area','name','location','des','avg_price']]
    # print(res['data'])

    
    # res['data'] = res['data'].reset_index(drop=True).to_dict(orient='index')
    # res['cnt'] = len(res['data'])
    
    return json.dumps(res, ensure_ascii=False)

# @app.route('/insert', methods=['POST', 'GET'])
# @cross_origin()
# def read_csv():
#     print(1111)
#     df.rename(columns={'年份':'year','环':'ring'}, inplace = True)
    
#     for index, row in df.iterrows():#保存的列名
#         house = House(lianjiaId=row.lianjia_id,title=row.title,follower_num=row.follower_num,total_price=row.total_price,area=row.area,avg_price=row.avg_price,directions=row.directions,floor=row.floor,year=row.year,decoration=row.decoration,location=row.location, \
#             school=row.school,mall=row.mall,medicine=row.medicine,traffic=row.traffic,total_floor=row.total_floor,ring=row.ring,room=row.room,parlor=row.parlor,kitchen=row.kitchen,toilet=row.toilet,district=row.district,block=row.block,name=row.name,address=row.address,des=row.des,community=row.community)
#         db.session.add(house)
#         if index%100==0:
#             print(index)
#     db.session.commit()
#     return jsonify({
#         'code':200,
#         'msg':'finish'
#     })

@app.route('/test', methods=['POST', 'GET'])
@cross_origin()
def test():
    tmp = House.query
    tmp = tmp.filter(House.total_price > 5, House.total_price < 10)
    tmp = tmp.filter(House.area > 100, House.area < 150)
    tmp = tmp.limit(10).offset((2-1)*10).first()
    print(tmp.__dict__)
    return str(tmp[0].to_json())

