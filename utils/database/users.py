import psycopg2


def connect_db():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='geeks',
        user='postgres',
        password='1234',
    )
    conn.autocommit = True
    return conn


def closed_db(conn):
    if conn:
        conn.close()


def create_user(fio, chat_id, username):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO users(fio, chat_id, username) VALUES ('{fio}','{chat_id}','{username}');")
    closed_db(conn)


def update_user(phone, chat_id):
    conn = connect_db()

    with conn.cursor() as cursor:
        cursor.execute(f"UPDATE users SET phone= '{phone}' where chat_id='{chat_id}'; ")



    closed_db(conn)


def delete_user(chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE chat_id = '{chat_id}';")
    conn.commit()

    closed_db(conn)


def select_users_by_id(chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"select * from users where chat_id='{chat_id}'",

        )
        result = cursor.fetchone()
    closed_db(conn)
    return result
def get_user():
    conn=connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            "select * from users"
        )
        result=cursor.fetchall()
    closed_db(conn)
    return result
