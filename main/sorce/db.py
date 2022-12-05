import mysql.connector as mydb

def conn_db():
    conn = mydb.connect(
        host = 'hack-u-mysql', #dbのコンテナ名
        port = '3306',
        user = 'root',
        password = 'pass',
        db = 'hack-u-db'
    )
    return conn


def insert(money_min, money_max, age, sex, relationship, topic1, topic2, topic3, topic4, topic5, UserRes):
    conn = conn_db()
    cur = conn.cursor()
    sql = ("insert into presents (money_min, money_max, age, sex, relationship, topic1, topic2, topic3, topic4, topic5, user_res)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    cur.execute(sql, (money_min, money_max, age, sex, relationship, topic1, topic2, topic3, topic4, topic5, UserRes))

    conn.commit()





    