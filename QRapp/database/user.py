from . import cursor, gres


def add_user(username, email, password):
    cursor.execute("""
                   INSERT INTO users (username, email, password)
                   VALUES (%s, %s, %s)
                   """, (username, email, password))
    gres.commit()


def get_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    row = cursor.fetchone()
    return row

