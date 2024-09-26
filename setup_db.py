import sqlite3

def view_by_url(id):
    id = str(int(id) % 382)
    conn = sqlite3.connect("bookmarks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookmarks WHERE id=?", (id,))
    rows = cur.fetchall()
    conn.close()
    return rows