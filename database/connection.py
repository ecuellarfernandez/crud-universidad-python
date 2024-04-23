import psycopg2


def create_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="universidad",
        user="postgres",
        password="root",
        port=5432
    )
    return conn


def execute_query(query, param=None):
    conn = create_connection()
    cursor = conn.cursor()
    if param:
        cursor.execute(query, param)
    else:
        cursor.execute(query)
    if query.lower().startswith('select'):
        result = cursor.fetchall()
    else:
        conn.commit()
        result = True
    cursor.close()
    conn.close()
    return result