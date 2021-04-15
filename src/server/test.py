from flask import Flask, request
# from flask_cors import cross_origin
import pandas as pd
import json
from config import dic_street
import joblib
# from fuzzywuzzy import process, fuzz


app = Flask(__name__)

df = pd.read_csv('des.csv')
# df.rename(columns={'名称':'name','总价':'totalPrice','面积':'area','小区名':'community'}, inplace=True)

# @app.route('/', methods=['GET','POST'])
# def index():
#     return 'Hello World'

addr_set = set(df['community'].to_list())
lst = list(addr_set)
dic = {}
directions = ['north','south','east','west','northeast','southeast','northwest','southwest']
order = ['area', 'floor', 'structure', 'decoration', 'elevatorRate', 'heating', 'elevator', 'block_price', 'block_fee', 'school', 'mall', 'traffic', 'medicine', 'south', 'north', 'east', 'west', 'southeast', 'southwest', 'northeast', 'northwest', 'totalFloor', 'year', 'district', 'street', 'ring', 'room', 'parlor', 'kitchen', 'bathroom']
model = joblib.load('XGB_reg.dat')

# @app.route('/search_community', methods=['GET'])
# def search_community():
#     name = request.args.get("name", type=str)
#     return json.dumps(process.extract(name, addr_set, limit=10))

@app.route('/all', methods=['GET'])
def all():
    return json.dumps(lst, ensure_ascii=False)


@app.route('/write', methods=['GET'])
def write():
    index = request.args.get("index", type=str)
    name = request.args.get("name", type=str)
    address = request.args.get("address", type=str)
    dic[index] = {'name':name, 'address':address}
    return 'Hello World'

@app.route('/write_dict', methods=['GET'])
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
    # print(f"{min_price} {max_price}")


    print(f'{min_price} {max_price}')


    res = {}
    res['total'] = len(df)
    start, end = (page-1) * offset, page * offset - 1

    # 根据条件筛选
    price_rule = (lambda x: min_price < x < max_price) if max_price != 20 else (lambda x: min_price < x)
    area_rule = (lambda x: min_area < x < max_area) if max_area != 200 else (lambda x: min_area < x)
    tmp = df[df['total_price'].apply(price_rule)]
    tmp = tmp[tmp['area'].apply(area_rule)]
    if district:
        tmp = tmp[tmp['district'] == district]
    if block:
        tmp = tmp[tmp['block'] == block]

    # 排序
    if sort_by == 1:
        tmp.sort_values(by="total_price", ascending=[False,True][sort_rule], inplace=True)

    res['total'] = len(tmp)
    res['data'] = tmp.reset_index(drop=True).loc[start:end,['title','total_price','area','name','location','des','avg_price']]
    print(res['data'])

    
    res['data'] = res['data'].reset_index(drop=True).to_dict(orient='index')
    res['cnt'] = len(res['data'])
    
    return json.dumps(res, ensure_ascii=False)



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
