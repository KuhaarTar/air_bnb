from sqlalchemy.orm import relationship

from app import db


class ReservationOrder(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    start_date = db.Column(db.DATETIME, nullable=False)
    end_date = db.Column(db.DATETIME, nullable=False)
    apartment_id = db.Column(db.BIGINT, db.ForeignKey('apartment.id'), nullable=False)
    renter_id = db.Column(db.BIGINT, db.ForeignKey('renter.id'), nullable=False)
    apartment = relationship("Apartment", back_populates="reservation_orders")
    renter = relationship("Renter", back_populates="reservation_orders")
    reviews = relationship("Reviews", back_populates="reservation_order")
    
    def to_dict(self):
        return {
            'id': self.id,
            'is_confirmed': self.is_confirmed,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'apartment': self.apartment.to_dict() if self.apartment else None,
            'renter': self.renter.to_dict() if self.renter else None,
            'reviews': [review.to_dict() for review in self.reviews] if self.reviews else [],
        }