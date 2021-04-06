from flask import Flask, request
from flask_cors import cross_origin
import pandas as pd
import json


app = Flask(__name__)

df = pd.read_csv('data.csv')
df.rename(columns={'名称':'name','总价':'totalPrice','面积':'area','小区名':'community'}, inplace=True)

# @app.route('/', methods=['GET','POST'])
# def index():
#     return 'Hello World'

# @app.route('/predict', methods=['POST'])
# @cross_origin()
# def predict():
#     return "返回值"

@app.route('/getHouses', methods=['POST', 'GET'])
@cross_origin()
def get_houses():
    # tmp = df.loc[0:5,['name','totalPrice','area','community','location']].to_dict(orient='index')
    # return json.dumps([tmp[i] for i in tmp], ensure_ascii=False)
    page = request.args.get("page", type=int)
    offset = request.args.get("offset", type=int)
    min_price = request.args.get("minPrice", type=int)
    max_price = request.args.get("maxPrice", type=int)
    # print(f"{min_price} {max_price}")

    res = {}
    res['total'] = len(df)
    start, end = (page-1) * offset, page * offset - 1
    price_rule = (lambda x: min_price < x < max_price) if max_price != 2000 else (lambda x: min_price < x)
    res['data'] = df[df['totalPrice'].apply(price_rule)].reset_index(drop=True)
    res['total'] = len(res['data'])
    res['data'] = res['data'].loc[start:end,['name','totalPrice','area','community','location']]
    res['data'] = res['data'].to_dict(orient='index')
    return json.dumps(res, ensure_ascii=False)



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
