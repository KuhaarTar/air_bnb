from app.dao.review_dao import ReviewsDAO
from app.dto import ReviewsDTO


class ReviewsService:
    @staticmethod
    def create_review(description, point, renter_id, apartment_id, reservation_order_id):
        review = ReviewsDAO.create_review(description, point, renter_id, apartment_id, reservation_order_id)
        return ReviewsDTO(review.review_id, review.description, review.point,
                          review.renter, review.apartment, review.reservation_order)

    @staticmethod
    def get_reviews():
        reviews_list = ReviewsDAO.get_reviews()
        return [ReviewsDTO(review.review_id, review.description, review.point,
                           review.renter, review.apartment, review.reservation_order)
                for review in reviews_list]

    @staticmethod
    def get_review_by_id(review_id):
        review = ReviewsDAO.get_review_by_id(review_id)
        if review:
            return ReviewsDTO(review.review_id, review.description, review.point,
                              review.renter, review.apartment, review.reservation_order)
        else:
            return None

    @staticmethod
    def update_review(review_id, description=None, point=None, renter_id=None, apartment_id=None, reservation_order_id=None):
        updated_review = ReviewsDAO.update_review(review_id, description, point, renter_id, apartment_id, reservation_order_id)
        if updated_review:
            return ReviewsDTO(updated_review.review_id, updated_review.description, updated_review.point,
                              updated_review.renter, updated_review.apartment, updated_review.reservation_order)
        else:
            return None

    @staticmethod
    def delete_review(review_id):
        deleted_review = ReviewsDAO.delete_review(review_id)
        if deleted_review:
            return ReviewsDTO(deleted_review.review_id, deleted_review.description, deleted_review.point,
                              deleted_review.renter, deleted_review.apartment, deleted_review.reservation_order)
        else:
            return None
