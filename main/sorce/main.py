from flask import Flask, request, jsonify
import pandas
import db
import requests
# from Model import model 

# 診断結果をdbにインサートするAPI
# レコメンドするAPI

app = Flask(__name__)

@app.route("/recommend")
def recommend():
    data = request.get_json()

    requests = requests.post('http://hack-u-model:5050/model/recommend', json=data)
    return(requests.json())

@app.route("/questionnaire/userRes")
def userRes():

    j_data = request.get_json()

    moneyMin      =  j_data['moneyMin']
    moneyMax      =  j_data['moneyMax']
    age           =  j_data['age']
    sex           =  j_data['sex']
    relationship  =  j_data['relationship']
    topic1        =  j_data['topic1']
    topic2        =  j_data['topic2']
    topic3        =  j_data['topic3']
    topic4        =  j_data['topic4']
    topic5        =  j_data['topic5']  
    UserRes       =  j_data['UserRes']

    db.insert(moneyMin, moneyMax, age, sex, relationship, topic1, topic2, topic3, topic4, topic5, UserRes)

    return jsonify({"massege": "OK"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)