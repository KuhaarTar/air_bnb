from app import db


class ApartmentPhoto(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    photo_url = db.Column(db.String(700), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=True)
    apartment_id = db.Column(db.BIGINT, db.ForeignKey('apartment.id'), nullable=False)
