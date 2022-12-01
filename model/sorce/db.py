import pandas as pd
import sqlalchemy as sa

# dataframeでdbからセレクトする

url = f'mysql+pymysql://root:pass@hack-u-mysql:3306/hack-u-db?charset=utf8'

engine = sa.create_engine(url, echo=False)


def make_df():
    query = f"select * from presents"
    df = pd.read_sql(query, con=engine)
    return df

# def make_df(user_id):
#     query = f"select * from presents where user_id = {user_id}"
#     df = pd.read_sql(query, con=engine)
#     return df