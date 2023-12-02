from sqlalchemy.orm import relationship

from app import db


class Address(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(50), nullable=False)
    country_name = db.Column(db.String(50), nullable=False)
    geo_location = db.Column(db.String(150), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    building = db.Column(db.String(45), nullable=False)
    flat = db.Column(db.String(45), nullable=True)
    apartment = relationship("Apartment", back_populates="address")

    def to_dict(self):
        return {
            'id': self.id,
            'city_name': self.city_name,
            'country_name': self.country_name,
            'geo_location': self.geo_location,
            'street': self.street,
            'building': self.building,
            'flat': self.flat
        }
