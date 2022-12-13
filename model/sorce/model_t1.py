import pandas as pd
import copy
import xgboost as xgb
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class AModel:
    def __init__(self):
        self.cluster_df = None
        self.model = None

    def make_cluster(self, input_df):
        sc = StandardScaler()
        df = copy.deepcopy(input_df)
        df_sc = sc.fit_transform(df.drop('name',axis=1))
        df_sc = pd.DataFrame(df_sc)

        cluster_model = KMeans(n_clusters=3, random_state=1)
        cluster_model.fit(df_sc)

        cluster = cluster_model.labels_
        df['cluster'] = cluster

        self.cluster_df = df

    def make_model(self, input_df: pd.DataFrame):
        self.make_cluster(input_df)
        cluster_df = copy.deepcopy(self.cluster_df)
        df_x = cluster_df.drop(['cluster','name'], axis=1)
        df_y = cluster_df['cluster']

        dtrain = xgb.DMatrix(df_x, df_y)

        num_class = len(df_y.unique())
        params = {
            'objective': 'multi:softmax',
            'silent': 1,
            'random_state': 1,
            'num_class': num_class
        }
        num_round = 10

        model = xgb.train(params, dtrain, num_round)

        self.model = model

    def pred(
            self,
            situation: pd.DataFrame
    ):
        model = self.model
        cluster_df = copy.deepcopy(self.cluster_df)

        # 属するクラスタの予測
        pred_ = model.predict(xgb.DMatrix(situation))
        cluster_num = pred_[0]

        cluster_num = round(cluster_num)

        df = cluster_df[cluster_df['cluster'] == cluster_num]
        reco_dict = df['name'].value_counts().to_dict()

        sort_list = sorted(reco_dict.items(), key=lambda x: x[1], reverse=True)

        reco_list = []
        for x in sort_list:
            reco_list.append(x[0])

        return reco_list[:6]


if __name__ == '__main__':

    path = 'model.csv'
    _input_df = pd.read_csv(path)

    #受け取ったデータをlにいれる
    l = [[2,2,1,1,1,1,1,1,1,1]]
    sample = pd.DataFrame(l, columns=['moneyMin','moneyMax','age','sex','season','topic1','topic2','topic3','topic4','topic5'])

    a_model = AModel()
    a_model.make_model(_input_df)
    reco_list = a_model.pred(sample)

    print(reco_list)