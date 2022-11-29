import pandas as pd
import sqlalchemy as sa
import mysql.connector as mydb

url = f'mysql+pymysql://root:pass@hack-u-mysql:3306/hack-u-db?charset=utf8'

engine = sa.create_engine(url, echo=False)

def conn_db():
    conn = mydb.connect(
        host = 'hack-u-mysql', #dbのコンテナ名
        port = '3306',
        user = 'root',
        password = 'pass',
        db = 'hack-u-db'
    )
    return conn

def make_df(user_id):
    query = f"select * from presents where user_id = {user_id}"
    df = pd.read_sql(query, con=engine)
    return df

def insert(user_id, month):
    conn = conn_db()
    cur = conn.cursor()
    sql = ("insert into presents (user_id, month)VALUES (%s, %s)")

    cur.execute(sql, (user_id, month))

    conn.commit()





    