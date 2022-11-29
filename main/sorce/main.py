from flask import Flask, request, jsonify
import pandas
import db
# from Model import model 

app = Flask(__name__)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    profile:pandas.DataFrame = pandas.DataFrame(data)
    return pandas.DataFrame.to_json(profile), 200

    # {"col1":{"user_id":"5","month":"8"}}こんな感じのリクエストじゃないとだめ

    # present_list = model.pred(profile)
    # return jsonify(present_list), 200

@app.route("/get")
def get():
    j_data = request.get_json()

    user_id    =  j_data['user_id']
    month      =  j_data['month']

    db.insert(user_id, month)

    # {"user_id":"5","month":"8"}

    return jsonify({"massege": "OK"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)