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

     # {"user_id":"5","age":"8"}てきなリクエストが飛んでくる

    j_data = request.get_json()

    user_id  =  j_data['user_id']
    age      =  j_data['age']

    db.insert(user_id, age)

    return jsonify({"massege": "OK"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)