from flask import Flask
from flask_cors import cross_origin
import pandas as pd
import json


app = Flask(__name__)

df = pd.read_csv('data.csv')

# @app.route('/', methods=['GET','POST'])
# def index():
#     return 'Hello World'

# @app.route('/predict', methods=['POST'])
# @cross_origin()
# def predict():
#     return "返回值"

@app.route('/predict', methods=['POST'])
@cross_origin()
def get_list():
    tmp = df.loc[0:5,['名称','总价','面积','小区名','location']].to_dict(orient='index')
    return json.dumps([tmp[i] for i in tmp], ensure_ascii=False)




if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
