from flask import Flask, request, jsonify
import schedule
from time import sleep
import pandas as pd
import db
import copy
import xgboost as xgb
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from flask_cors import CORS

import model_t1

app = Flask(__name__)
CORS(app)

Topic = [0] * 5
a_model = model_t1.AModel()

@app.route('/test', methods= ["POST"])
def test() :

    return jsonify({"recommends" : [{"name" : "suh"},{"name" : "jhsg"}, {"name" : "hjhu"}, {"name" : "hguu"}, {"name" : "hugu"}, {"name" : "hujhvu"}]})


@app.route("/model/recommend") # 機械学習にレコメンドさせてるとこ
def recommend():
    data = request.get_json()

    moneyMin      =  data['moneyMin']
    moneyMax      =  data['moneyMax']
    age           =  data['age']
    sex           =  data['sex']
    season        =  data['season']
    topic         =  data['topic']

    if age == 'around_10':
        Age = 1
    elif age == 'around_20':
        Age = 2
    elif age == 'around_30':
        Age = 3
    elif age == 'around_40':
        Age = 4
    elif age == 'around_50':
        Age = 5
    else:
        Age = 6

    if sex == 'male':
        Sex = 1
    elif sex == 'female':
        Sex = 2
    else:
        Sex = 3

    if season == 'spring':
        Season = 1
    elif season == 'summer':
        Season = 2
    elif season == 'autumn':
        Season = 3
    else:
        Season = 4
    
    if 'fashion' in topic:
        Topic[0] = 1
    if 'dailyNecessities' in topic:
        Topic[1] = 1
    if 'food' in topic:
        Topic[2] = 1
    if 'sports' in topic:
        Topic[3] = 1
    if 'entertainment' in topic:
        Topic[4] = 1

    u_data=[[moneyMin, moneyMax, Age, Sex, Season, Topic[0], Topic[1], Topic[2], Topic[3], Topic[4]]]
    culum=['moneyMin', 'moneyMax','age', 'sex', 'season', 'topic1', 'topic2', 'topic3', 'topic4', 'topic5']

    profile:pd.DataFrame = pd.DataFrame(u_data, columns=culum)

    print (profile)

    present_list = a_model.pred(profile)

    print(present_list)

    # return jsonify({"massage" : "ok"})
    return jsonify({
        "recomends": 
        [
            {"name" : present_list[0]}, 
            {"name" : present_list[1]}, 
            {"name" : present_list[2]}, 
            {"name" : present_list[3]}, 
            {"name" : present_list[4]}
        ]
        }), 200

if __name__ == "__main__":
    path = 'model.csv'
    _input_df = pd.read_csv(path)

    a_model.make_model(_input_df)    

    app.run(host="0.0.0.0", port=5050, debug=True)

    
    def make_model():
        model = model_t1.AModel()
        df : pd.DataFrame = db.select_df()
        return model.make_model(df)

    schedule.every(1).day.do(make_model)
    while True:
        schedule.run_pending()
        sleep(1)