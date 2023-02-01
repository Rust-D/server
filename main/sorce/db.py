import mysql.connector as mydb

# コネクション
def conn_db():
    conn = mydb.connect(
        host = 'hack-u-mysql', # dbのコンテナ名
        port = '3306',         # ポート番号
        user = 'root',         # ユーザーの名前
        password = 'pass',     # password
        db = 'hack-u-db'       # dbの名前
    )
    return conn

# DBに保存する関数
def insert(money_min, money_max, age, sex, season, topic1, topic2, topic3, topic4, topic5, UserRes):
    conn = conn_db()
    cur = conn.cursor()
    sql = ("insert into user_res (money_min, money_max, age, sex, season, topic1, topic2, topic3, topic4, topic5, user_res)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    cur.execute(sql, (money_min, money_max, age, sex, season, topic1, topic2, topic3, topic4, topic5, UserRes))

    conn.commit()





    