from flask import Flask, request
from flask_cors import cross_origin
import pandas as pd
import json


app = Flask(__name__)

df = pd.read_csv('en1.csv')
# df.rename(columns={'名称':'name','总价':'totalPrice','面积':'area','小区名':'community'}, inplace=True)

# @app.route('/', methods=['GET','POST'])
# def index():
#     return 'Hello World'

@app.route('/predict', methods=['POST'])
# @cross_origin()
def predict():
    return "返回值"

@app.route('/getHouses', methods=['POST', 'GET'])
# @cross_origin()
def get_houses():
    # tmp = df.loc[0:5,['name','totalPrice','area','community','location']].to_dict(orient='index')
    # return json.dumps([tmp[i] for i in tmp], ensure_ascii=False)
    page = request.args.get("page", type=int)
    offset = request.args.get("offset", type=int)
    min_price = request.args.get("minPrice", type=int)
    max_price = request.args.get("maxPrice", type=int)
    district = request.args.get("district", type=str)
    block = request.args.get("block", type=str)
    # print(f"{min_price} {max_price}")


    print(f'{district} {block}')


    res = {}
    res['total'] = len(df)
    start, end = (page-1) * offset, page * offset - 1

    # 根据条件筛选
    price_rule = (lambda x: min_price < x < max_price) if max_price != 2000 else (lambda x: min_price < x)
    tmp = df[df['total_price'].apply(price_rule)]
    if district:
        tmp = tmp[tmp['district'] == district]
    if block:
        tmp = tmp[tmp['block'] == block]

    res['total'] = len(tmp)
    res['data'] = tmp.reset_index(drop=True).loc[start:end,['title','total_price','area','community','location']]
    print(res['data'])
    res['data'] = res['data'].reset_index(drop=True).to_dict(orient='index')
    res['cnt'] = len(res['data'])
    
    return json.dumps(res, ensure_ascii=False)



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
