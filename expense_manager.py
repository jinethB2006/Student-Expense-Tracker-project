import sqlite3
import pandas as pd

# -------- CONNECTION --------
def get_conn():
    conn=sqlite3.connect("data/data.db",timeout=10)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=3000")
    return conn

# -------- INIT --------
def init_db():
    with get_conn() as conn:
        c=conn.cursor()

        c.execute("""create table if not exists expenses(
        id integer primary key,
        user_id int,
        date text,
        category text,
        amount real,
        note text)""")

        c.execute("""create table if not exists budget(
        user_id int,
        amount real)""")

init_db()

# -------- EXPENSE --------
def load_data(user_id):
    with get_conn() as conn:
        df=pd.read_sql_query(
            "select date,category,amount,note from expenses where user_id=?",
            conn,
            params=(user_id,)
        )
        return df

def add_expense(user_id,date,category,amount,note):
    with get_conn() as conn:
        c=conn.cursor()
        c.execute(
            "insert into expenses(user_id,date,category,amount,note) values(?,?,?,?,?)",
            (user_id,str(date),category,amount,note)
        )

def clear_expenses(user_id):
    with get_conn() as conn:
        c=conn.cursor()
        c.execute("delete from expenses where user_id=?",(user_id,))

# -------- BUDGET --------
def save_budget(user_id,amount):
    with get_conn() as conn:
        c=conn.cursor()
        c.execute("delete from budget where user_id=?",(user_id,))
        c.execute("insert into budget(user_id,amount) values(?,?)",(user_id,amount))

def load_budget(user_id):
    with get_conn() as conn:
        c=conn.cursor()
        c.execute("select amount from budget where user_id=?",(user_id,))
        data=c.fetchone()
        return data[0] if data else 0
