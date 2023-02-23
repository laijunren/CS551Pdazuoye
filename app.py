from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Artist(db.Model):
    artist_id = db.Column(db.String(20), primary_key=True)
    mbtag = db.relationship('ArtistMbtag', backref='artist_mbtag')
    term = db.relationship('ArtistTerm', backref='artist_term')

class ArtistMbtag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.String(20),db.ForeignKey('artist.artist_id'), nullable=False)
    mbtag = db.Column(db.String(120))

class ArtistTerm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.String(20),db.ForeignKey('artist.artist_id'), nullable=False)
    term = db.Column(db.String(50))



@app.route('/', methods=["GET",])
def index():
    artist_obj = Artist.query.all()
    if request.method== "POST":
        pass
    print(artist_obj)
    return render_template("index.html",artist_obj=artist_obj)


if __name__ == '__main__':
    app.run()
