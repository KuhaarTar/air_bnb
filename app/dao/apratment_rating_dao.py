from app import db
from app.models import ApartmentRating


class ApartmentRatingDAO:
    @staticmethod
    def create_apartment_rating(count_of_reviews, avg_point, time_created, time_modified):
        apartment_rating = ApartmentRating(
            count_of_reviews=count_of_reviews,
            avg_point=avg_point,
            time_created=time_created,
            time_modified=time_modified
        )
        db.session.add(apartment_rating)
        db.session.commit()
        return apartment_rating

    @staticmethod
    def get_apartment_rating(rating_id):
        return ApartmentRating.query.get(rating_id)

    @staticmethod
    def get_apartment_ratings():
        return ApartmentRating.query.all()

    @staticmethod
    def get_apartment_rating_by_id(id):
        return ApartmentRating.query.get(id)

    @staticmethod
    def update_apartment_rating(rating_id, count_of_reviews=None, avg_point=None,  time_created =None,time_modified=None):
        apartment_rating = ApartmentRatingDAO.get_apartment_rating(rating_id)

        if apartment_rating:
            if count_of_reviews is not None:
                apartment_rating.count_of_reviews = count_of_reviews
            if avg_point is not None:
                apartment_rating.avg_point = avg_point
            if time_modified is not None:
                apartment_rating.time_modified = time_modified
            if time_created is not None:
                apartment_rating.time_created = time_created

            db.session.commit()

        return apartment_rating

    @staticmethod
    def delete_apartment_rating(rating_id):
        apartment_rating = ApartmentRatingDAO.get_apartment_rating(rating_id)

        if apartment_rating:
            db.session.delete(apartment_rating)
            db.session.commit()

        return apartment_rating
