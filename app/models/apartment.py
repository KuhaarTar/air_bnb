from sqlalchemy.orm import relationship

from app import db


class Apartment(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    area_of_territory = db.Column(db.String(45), nullable=False)
    enable_to_reserve = db.Column(db.Boolean, nullable=False, default=True)
    cost_per_hour = db.Column(db.String(45), nullable=False)
    lessor_id = db.Column(db.BIGINT, db.ForeignKey('lessor.id'), nullable=False)
    address_id = db.Column(db.BIGINT, db.ForeignKey('address.id'), nullable=False)
    rating_id = db.Column(db.BIGINT, db.ForeignKey('apartment_rating.rating_id'), nullable=False, unique=True)
    reservation_orders = relationship("ReservationOrder", back_populates="apartment")
    lessor = relationship("Lessor", back_populates="apartments")
    address = relationship("Address", back_populates="apartment")
    rating = relationship("ApartmentRating", back_populates="apartment")
    reviews = relationship("Reviews", back_populates="apartment")

    def to_dict(self):
        return {
            'id': self.id,
            'area_of_territory': self.area_of_territory,
            'enable_to_reserve': self.enable_to_reserve,
            'cost_per_hour': self.cost_per_hour,
            'lessor': self.lessor.to_dict(),
            'address': self.address.to_dict(),
            'rating': self.rating.to_dict()
        }
