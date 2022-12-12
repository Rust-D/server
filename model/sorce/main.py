from flask import Flask, request, jsonify
import schedule
from time import sleep
import pandas
import db

from model_t1 import AModel

model = AModel

app = Flask(__name__)

Topic = [False] * 5

@app.route("/model/recommend") # 機械学習にレコメンドさせてるとこ
def recommend():
    data = request.get_json()

# {
#     "moneyMin": 1000,
#     "moneyMax": 10000,
#     "age":      "around_10",
#     "sex":      "mare",
#     "season":   "spring",
#     "topic":    ["fashion", "sports"]
# }

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
        Topic[0] = True
    if 'dailyNecessities' in topic:
        Topic[1] = True
    if 'food' in topic:
        Topic[2] = True
    if 'sports' in topic:
        Topic[3] = True
    if 'entertainment' in topic:
        Topic[4] = True

    u_data=[[moneyMin, moneyMax, Age, Sex, Season, Topic[0], Topic[1], Topic[2], Topic[3], Topic[4]]]
    culum=['moneyMin', 'moneyMax','age', 'sex', 'season', 'topic1', 'topic2', 'topic3', 'topic4', 'topic5']

    profile:pandas.DataFrame = pandas.DataFrame(u_data, culumns=culum)

    present_list = model.pred(profile)
    return jsonify({"recomends": present_list}), 200

def make_model():
    df : pandas.DataFrame = db.select_df()
    return model.make_model(df)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
    schedule.every(1).day.do(make_model)
    while True:
        schedule.run_pending()
        sleep(1)