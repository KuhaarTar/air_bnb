from app import db
from app.models import Reviews


class ReviewsDAO:
    @staticmethod
    def create_review(description, point, renter, apartment, reservation_order):
        review = Reviews(
            description=description,
            point=point,
            renter=renter,
            apartment=apartment,
            reservation_order=reservation_order
        )
        db.session.add(review)
        db.session.commit()
        return review

    @staticmethod
    def get_reviews():
        return Reviews.query.all()

    @staticmethod
    def get_review_by_id(review_id):
        return Reviews.query.get(review_id)

    @staticmethod
    def get_all_by_renter(renter_id):
        return Reviews.query.all().filter(Reviews.renter == renter_id)

    @staticmethod
    def update_review(review_id, description=None, point=None, renter=None, apartment=None, reservation_order=None):
        review = ReviewsDAO.get_review_by_id(review_id)

        if review:
            if description:
                review.description = description
            if point is not None:
                review.point = point
            if renter:
                review.renter = renter
            if apartment:
                review.apartment = apartment
            if reservation_order:
                review.reservation_order = reservation_order

            db.session.commit()

        return review

    @staticmethod
    def delete_review(review_id):
        review = ReviewsDAO.get_review_by_id(review_id)

        if review:
            db.session.delete(review)
            db.session.commit()

        return review
