from app import db


class Amenities(db.Model):
    amenities_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(150), nullable=False)