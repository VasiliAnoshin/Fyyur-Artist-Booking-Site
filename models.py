from init import db

class Show(db.Model):
     __tablename__ = 'Show'

     id = db.Column(db.Integer, primary_key=True)
     artist_id  = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable = False)
     venue_id   = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable = False)
     start_time = db.Column(db.DateTime())

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500), nullable = True)
    facebook_link = db.Column(db.String(120),)
    genres = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False, nullable=False)
    seeking_description = db.Column(db.String(360))
    website = db.Column(db.String(120))
    shows = db.relationship("Show", backref='venue', lazy = True)


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500),nullable = True)
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False, nullable=False)
    seeking_description = db.Column(db.String(360))
    website = db.Column(db.String(120))
    shows = db.relationship("Show", backref='artist', lazy = True)
