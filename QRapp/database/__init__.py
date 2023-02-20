import psycopg2

gres = psycopg2.connect(

    host='kashin.db.elephantsql.com',
    port=5432,
    user='iywbfzuv',
    database='iywbfzuv',
    password='BWqYOLr3lh9mY6Ud8Rp7eM2orUJbQGjc'

)

cursor = gres.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id SERIAL UNIQUE,               
                username VARCHAR(30) UNIQUE NOT NULL, 
                email VARCHAR(30) UNIQUE NOT NULL, 
                password VARCHAR(30) NOT NULL); 
               """)

gres.commit()


cursor.execute("""
                CREATE TABLE IF NOT EXISTS qr_codes (
                id SERIAL UNIQUE,
                owner INT references users(id),
                data TEXT NOT NULL
    )
""")
gres.commit()

