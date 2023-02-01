from flask import Flask, request, jsonify
import db
import requests

from flask_cors import CORS

app = Flask(__name__)
api = Flask(__name__)

CORS(app)

# クロスオリジンを許可する
@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers' 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods' 'GET,POST')

Topic = [0] * 5

# 推論するときののAPI、機械学習コンテナにリクエストを投げる
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    res = requests.get('http://hack-u-model:5050/model/recommend', json=data)
    return(res.json())

# 学習データを集めるときのAPI、DBに保存する
@app.route("/questionnaire/userRes")
def userRes():

    j_data = request.get_json()

    moneyMin    =  j_data['moneyMin']
    moneyMax    =  j_data['moneyMax']
    age         =  j_data['age']
    sex         =  j_data['sex']
    season      =  j_data['season']
    topic       =  j_data['topic']
    UserRes     =  j_data['UserRes']

    if age == 'around_10':
        Age = 0
    elif age == 'around_20':
        Age = 1
    elif age == 'around_30':
        Age = 2
    elif age == 'around_40':
        Age = 3
    elif age == 'around_50':
        Age = 4
    else:
        Age = 5

    if sex == 'male':
        Sex = 0
    elif sex == 'female':
        Sex = 1
    else:
        Sex = 2

    if season == 'spring':
        Season = 0
    elif season == 'summer':
        Season = 1
    elif season == 'autumn':
        Season = 2
    else:
        Season = 3
    
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

    db.insert(moneyMin, moneyMax, Age, Sex, Season, Topic[0], Topic[1], Topic[2], Topic[3], Topic[4], UserRes)

    return jsonify({"massege": "OK"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)