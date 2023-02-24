import sqlite3

from flask import Flask, render_template, request, g

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect('artist_style.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    try:
        return g.db
    except:
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

@app.route('/artist_mgtag', methods=["GET",])
def artist_mgtag():
    db = create_db()
    # Sql counts the number of mbtag de-duplicated from the mbtag artist
    cur = db.execute("select count(distinct mbtag) from mbtag_artist")
    mbtag_num = cur.fetchall()
    # Get the duplicate mbtag from the database
    cur = db.execute("select distinct mbtag from mbtag_artist")
    mbtag_list = cur.fetchall()
    # Sql counts the top 10 artist ids with the most mbtag from the mbtag artist and displays the number of them in the format: artist id, mbtag num
    cur = db.execute("select artist_id,count(mbtag) from mbtag_artist group by artist_id order by count(mbtag) desc limit 10")
    mbtag_artist = cur.fetchall()
    # Sql counts the top 10 mbtabs with the highest number of occurrences of mbtag in the mbtag artist table. The display format is: mbtag, number of occurrences
    cur = db.execute("select mbtag,count(mbtag) from mbtag_artist group by mbtag order by count(mbtag) desc limit 10")
    mbtag_top = cur.fetchall()

    if mbtag_num[0][0] and mbtag_artist and mbtag_list and mbtag_top:
        return render_template("artistmbtag.html",mbtag_num = mbtag_num[0][0],mbtag_artist = mbtag_artist,mbtag_list = mbtag_list,mbtag_top=mbtag_top)
    else:
        return render_template("artistmbtag.html")


if __name__ == '__main__':
    app.run()
