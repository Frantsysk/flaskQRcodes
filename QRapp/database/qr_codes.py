from . import cursor, gres


def add_qr(owner, data):
    cursor.execute("""
            INSERT INTO qr_codes (owner, data)
            VALUES (%s, %s) RETURNING id
            """, (owner, data))
    u_id = cursor.fetchone()[0]
    gres.commit()
    return u_id


def get_qr(owner):
    cursor.execute("SELECT * FROM qr_codes WHERE owner = %s", (owner,))
    rows = cursor.fetchall()
    return rows


def get_qr_by_id(id):
    cursor.execute("SELECT data FROM qr_codes WHERE id = %s", (id,))
    data = cursor.fetchone()[0]
    return data




