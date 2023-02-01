import pandas as pd
import sqlalchemy as sa

url = 'mysql+pymysql://root:pass@hack-u-mysql:3306/hack-u-db?charset=utf8'
    # 'dbの種類+ドライバ://username:password@IP:port/dbname?文字コード'

engine = sa.create_engine(url, echo=False)

def select_df():
    query = f"select * from user_res"
    df = pd.read_sql(query, con=engine)
    return df
