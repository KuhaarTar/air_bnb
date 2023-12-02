from app.dto import ApartmentRatingDTO
from app.dao.apratment_rating_dao import ApartmentRatingDAO


class ApartmentRatingService:
    @staticmethod
    def create_apartment_rating(count_of_reviews, avg_point, time_created, time_modified):
        rating = ApartmentRatingDAO.create_apartment_rating(count_of_reviews, avg_point, time_created, time_modified)
        return ApartmentRatingDTO(rating.rating_id, rating.count_of_reviews, rating.avg_point, rating.time_created,
                                  rating.time_modified)

    @staticmethod
    def get_apartment_ratings():
        ratings = ApartmentRatingDAO.get_apartment_ratings()
        return [ApartmentRatingDTO(rating.rating_id, rating.count_of_reviews, rating.avg_point, rating.time_created,
                                   rating.time_modified) for rating in ratings]

    @staticmethod
    def get_apartment_rating_by_id(rating_id):
        rating = ApartmentRatingDAO.get_apartment_rating_by_id(rating_id)
        if rating:
            return ApartmentRatingDTO(rating.rating_id, rating.count_of_reviews, rating.avg_point, rating.time_created,
                                      rating.time_modified)
        else:
            return None

    @staticmethod
    def update_apartment_rating(rating_id, count_of_reviews=None, avg_point=None, time_created=None,
                                time_modified=None):
        updated_rating = ApartmentRatingDAO.update_apartment_rating(rating_id, count_of_reviews, avg_point,
                                                                    time_created, time_modified)
        if updated_rating:
            return ApartmentRatingDTO(updated_rating.rating_id, updated_rating.count_of_reviews,
                                      updated_rating.avg_point, updated_rating.time_created,
                                      updated_rating.time_modified)
        else:
            return None

    @staticmethod
    def delete_apartment_rating(rating_id):
        deleted_rating = ApartmentRatingDAO.delete_apartment_rating(rating_id)
        if deleted_rating:
            return ApartmentRatingDTO(deleted_rating.rating_id, deleted_rating.count_of_reviews,
                                      deleted_rating.avg_point, deleted_rating.time_created,
                                      deleted_rating.time_modified)
        else:
            return None
