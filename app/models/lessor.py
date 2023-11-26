from sqlalchemy.orm import relationship

from app import db


class Lessor(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    apartments = relationship("Apartment", back_populates="lessor")

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'phone': self.phone,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
