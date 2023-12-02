from sqlalchemy.orm import relationship

from app import db


class Reviews(db.Model):
    review_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    description = db.Column(db.String(500), nullable=True)
    point = db.Column(db.Float, nullable=False)
    renter_id = db.Column(db.BIGINT, db.ForeignKey('renter.id'), nullable=False)
    apartment_id = db.Column(db.BIGINT, db.ForeignKey('apartment.id'), nullable=False)
    reservation_order_id = db.Column(db.BIGINT, db.ForeignKey('reservation_order.id'), nullable=False)
    reservation_order = relationship("ReservationOrder", back_populates="reviews")
    renter = relationship("Renter", back_populates="reviews")
    apartment = relationship("Apartment", back_populates="reviews")

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'description': self.description,
            'point': self.point,
            'renter': self.renter.to_dict() if self.renter else None,
            'apartment_id': self.apartment_id,
            'reservation_order_id': self.reservation_order_id,
        }
