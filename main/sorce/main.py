from flask import Flask, request, jsonify
import pandas
import db
import requests

from flask_cores import CORS
# from Model import model 

# 診断結果をdbにインサートするAPI
# レコメンドするAPI

app = Flask(__name__)
CORS(app)
@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers' 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods' 'GET,POST')

Topic = [False] * 5

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    res = requests.get('http://hack-u-model:5050/model/recommend', json=data)
    return(res.json())

@app.route("/questionnaire/userRes")
def userRes():

    j_data = request.get_json()

    moneyMin      =  j_data['moneyMin']
    moneyMax      =  j_data['moneyMax']
    age           =  j_data['age']
    sex           =  j_data['sex']
    season        =  j_data['season']
    topic         =  j_data['topic']
    UserRes       =  j_data['UserRes']

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
        Topic[0] = True
    if 'dailyNecessities' in topic:
        Topic[1] = True
    if 'food' in topic:
        Topic[2] = True
    if 'sports' in topic:
        Topic[3] = True
    if 'entertainment' in topic:
        Topic[4] = True

    db.insert(moneyMin, moneyMax, Age, Sex, Season, Topic[0], Topic[1], Topic[2], Topic[3], Topic[4], UserRes)

    return jsonify({"massege": "OK"}), 200

@app.route('/test', methods= ["POST"])
def test() :

    return jsonify({"recommends" : [{"name" : "suh"},{"name" : "jhsg"}, {"name" : "hjhu"}, {"name" : "hguu"}, {"name" : "hugu"}, {"name" : "hujhvu"}]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)