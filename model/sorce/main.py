from flask import Flask, request, jsonify
import schedule
from time import sleep
import pandas
import db

app = Flask(__name__)

@app.route("/model/recommend", methods=["POST"]) # 機械学習にレコメンドさせてるとこ
def recommend():
    data = request.get_json()

    profile:pandas.DataFrame = pandas.DataFrame(data)

    present_list = model.pred(profile)
    return jsonify(present_list), 200

def make_model():
    df : pandas.DataFrame = db.select_df()
    return model.make_model(df)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
    schedule.every(1).day.do(make_model)
    while True:
        schedule.run_pending()
        sleep(1)