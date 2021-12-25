import psycopg2
import os


def create_table():
    password = os.environ.get("PASSWORD")
    conn = psycopg2.connect(f"dbname='first database'"
                            f" user='postgres'"
                            f" password='{password}'"
                            f" host='localhost'"
                            f" port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    password = os.environ.get("PASSWORD")
    conn = psycopg2.connect(f"dbname='first database'"
                            f" user='postgres'"
                            f" password='{password}'"
                            f" host='localhost'"
                            f" port='5432'")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO store VALUES('{item}', {quantity}, {price})")
    conn.commit()
    conn.close()


def view():
    password = os.environ.get("PASSWORD")
    conn = psycopg2.connect(f"dbname='first database'"
                            f" user='postgres'"
                            f" password='{password}'"
                            f" host='localhost'"
                            f" port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    password = os.environ.get("PASSWORD")
    conn = psycopg2.connect(f"dbname='first database'"
                            f" user='postgres'"
                            f" password='{password}'"
                            f" host='localhost'"
                            f" port='5432'")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM store WHERE item = {item}")
    conn.commit()
    conn.close()


def update(item, quantity, price):
    password = os.environ.get("PASSWORD")
    conn = psycopg2.connect(f"dbname='first database'"
                            f" user='postgres'"
                            f" password='{password}'"
                            f" host='localhost'"
                            f" port='5432'")
    cur = conn.cursor()
    cur.execute(f"UPDATE store SET quantity={quantity}, price={price} WHERE item={item}")
    conn.commit()
    conn.close()


print(view())
