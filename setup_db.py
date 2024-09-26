import sqlite3
from pprint import pp 

def create_table():
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookmarks(id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT, name TEXT)")
    conn.commit()
    conn.close()

def insert(bookmark_name, url):
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO bookmarks (url, name) VALUES (?, ?)", (url, bookmark_name))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookmarks")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(name):
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM bookmarks WHERE name={name}")
    conn.commit()
    conn.close()

def update_by_id(id, new_name):
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute("UPDATE bookmarks SET name=? WHERE id=?", (new_name, id))
    conn.commit()
    conn.close()

def update_by_name(name, new_name):
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute("UPDATE bookmarks SET name=? WHERE name=?", (new_name, name))
    conn.commit()
    conn.close()

def search_by_name(name):
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookmarks WHERE name LIKE ?", ('%' + name + '%',))
    rows = cur.fetchall()
    conn.close()
    return rows

def search_by_url(url):
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookmarks WHERE url LIKE ?", ('%' + url + '%',))
    rows = cur.fetchall()
    conn.close()
    return rows

create_table()
insert("UMD", "www.umdearborn.edu")
insert("Google", "www.google.com")
insert("Wikipedia", "www.wikipedia.org")
insert("Microsoft", "www.microsoft.com")
insert("Linux", "www.linux.org")
update_by_name("Google", "Bing")
pp(view())
