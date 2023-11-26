from app import db


class ApartmentHasAmenities(db.Model):
    amenities_id = db.Column(db.BIGINT, db.ForeignKey('amenities.amenities_id'), nullable=False, primary_key=True)
    apartment_id = db.Column(db.BIGINT, db.ForeignKey('apartment.id'), nullable=False, primary_key=True)
