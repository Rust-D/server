import pandas as pd
import copy
import xgboost as xgb
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

class Amodel:
    def __init__(self): #インスタンス生成
        self.model = None
        self.cluster_df = None


    def make_cluster(self,input):
        ss = StandardScaler() #標準化のオブジェクト
        df = copy.deepcopy(input)
        df_ss = ss.fit_transform(df.drop('name',axis = 1))
        df_ss = pd.DataFrame(df_ss)
        input_s = copy.deepcopy(df_ss)

        #エルボー法で最適なクラスを決める ↓

        pca = PCA(n_components=2, random_state=1) #主成分分析の次元削減(PCA)実行
        pca.fit(df_ss)
        feature = pca.transform(df_ss)

        distortions = []
        b = 0
        dif_l = []

        for i in range(1,9):
            inspection = KMeans(n_clusters=i,
                         random_state=0)

            inspection.fit(df_ss)
            distortions.append(inspection.inertia_)
            #print('Distortion: %.2f'% inspection.inertia_)

            a = inspection.inertia_

            dif = b-a
            #print('dif = %.2f'% dif)
            dif_l.append(dif)
    
            b = inspection.inertia_

        dif_b = 0
        max_o = 0

        for i in range(1,7):

            dif_a = dif_l[i]
            #print('dif_a:%.2f'% dif_a)
            optimum = dif_b / dif_a
            #print(optimum)
            dif_b = dif_l[i]
            #print('dif_b:%.2f'% dif_b)
            
            if optimum > max_o:
                max_o = optimum
                num = i  #最適なクラスタ数


        cluster_model = KMeans(n_clusters=i) #クラスタリングのモデル作成
        cluster_model.fit(df_ss)

        cluster = cluster_model.labels_  #clusterというcluster_modelによってできるあたらしいラベルを定義
        df['cluster'] = cluster  #dfに新しいラベルを用意してあげる

        self.input_s = input_s
        self.cluster_df = df 

    def make_model(self, input_df: pd.DataFrame):
        self.make_cluster(input_df) #クラスタリングのメソッド呼び出し
        cluster_df = copy.deepcopy(self.cluster_df)
        df_x = cluster_df.drop(['cluster','name'], axis=1) #名前とクラスタ数の列を消す
        df_y = cluster_df['cluster'] #clusterを正解データとする

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
            reco_list.append(x[0])  #新しいリストを定義し、sort_listからデータを挿入

        return reco_list[:6]



if __name__ == '__main__':
    path = 'rust-d\model.csv'
    _input = pd.read_csv(path)

    #受け取ったデータをlにいれる
    l = [[2000,12000,1,1,3,1,0,0,0,0]]
    sample = pd.DataFrame(l, columns=['moneyMin','moneyMax','age','sex','season','topic1','topic2','topic3','topic4','topic5'])

    model = Amodel()
    model.make_model(_input)
    reco_list = model.pred(sample)

    print(reco_list)


