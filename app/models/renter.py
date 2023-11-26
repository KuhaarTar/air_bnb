from sqlalchemy.orm import relationship

from app import db


class Renter(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    phone = db.Column(db.String(150), nullable=False)
    reservation_orders = relationship("ReservationOrder", back_populates="renter")
    reviews = relationship("Reviews", back_populates="renter")  # Add this line

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'reservation_orders': [order.to_dict() for order in self.reservation_orders] if self.reservation_orders else [],
            'reviews': [review.to_dict() for review in self.reviews] if self.reviews else [],
        }
