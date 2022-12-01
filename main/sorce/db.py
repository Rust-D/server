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


def insert(user_id, month):
    conn = conn_db()
    cur = conn.cursor()
    sql = ("insert into presents (user_id, month)VALUES (%s, %s)")

    cur.execute(sql, (user_id, month))

    conn.commit()





    