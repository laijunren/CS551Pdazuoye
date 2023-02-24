import sqlite3

from flask import Flask, render_template, request, g

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect('artist_style.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    if g.db:
        return g.db
    else:
        g.db = conn
        return g.db


@app.route('/', methods=["GET",])
def index():
    db = create_db()
    cur = db.execute("select count(*) from artist")
    artist_num = cur.fetchall()
    if artist_num[0][0]:
        return render_template("index.html",artist_num=artist_num[0][0])
    else:
        return render_template("index.html", artist_obj=100)


if __name__ == '__main__':
    app.run()
