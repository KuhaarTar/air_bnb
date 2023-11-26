from sqlalchemy.orm import relationship

from app import db


class ApartmentRating(db.Model):
    rating_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    count_of_reviews = db.Column(db.Integer, nullable=False)
    avg_point = db.Column(db.Float, nullable=False)
    time_created = db.Column(db.DATETIME, nullable=False)
    time_modified = db.Column(db.DATETIME, nullable=False)
    apartment = relationship("Apartment", back_populates="rating")

    def to_dict(self):
        return {
            'rating_id': self.rating_id,
            'count_of_reviews': self.count_of_reviews,
            'avg_point': self.avg_point,
            'time_created': self.time_created,
            'time_modified': self.time_modified
        }
