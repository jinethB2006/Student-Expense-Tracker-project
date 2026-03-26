import sqlite3,hashlib

def get_conn():
    conn=sqlite3.connect("data/data.db",timeout=10)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=3000")
    return conn

def hash_pass(p):
    return hashlib.sha256(p.encode()).hexdigest()

def create_users_table():
    with get_conn() as conn:
        c=conn.cursor()
        c.execute("""
        create table if not exists users(
        id integer primary key,
        username text,
        password text)
        """)

create_users_table()

def signup(u,p):
    with get_conn() as conn:
        c=conn.cursor()
        c.execute("create table if not exists users(id integer primary key,username text,password text)")
        c.execute("insert into users(username,password) values(?,?)",(u,hash_pass(p)))

def login(u,p):
    with get_conn() as conn:
        c=conn.cursor()
        c.execute("select * from users where username=? and password=?",(u,hash_pass(p)))
        return c.fetchone()
