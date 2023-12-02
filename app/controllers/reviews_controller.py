from flask import jsonify, request
from app.services.reviews_service import ReviewsService
from app import app


@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    description = data.get('description')
    point = data.get('point')
    renter_id = data.get('renter_id')
    apartment_id = data.get('apartment_id')
    reservation_order_id = data.get('reservation_order_id')

    if not description or point is None or not renter_id or not apartment_id or not reservation_order_id:
        return jsonify(
            {'error': 'description, point, renter_id, apartment_id, and reservation_order_id are required'}), 400

    review_dto = ReviewsService.create_review(description, point, renter_id, apartment_id, reservation_order_id)
    return jsonify(review_dto.to_dict()), 201


@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews_list = ReviewsService.get_reviews()
    return jsonify([review.to_dict() for review in reviews_list])


@app.route('/reviews/<int:review_id>', methods=['GET'])
def get_review_by_id(review_id):
    review_dto = ReviewsService.get_review_by_id(review_id)
    if review_dto:
        return jsonify(review_dto.to_dict())
    else:
        return jsonify({'error': 'Review not found'}), 404


@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    description = data.get('description')
    point = data.get('point')
    renter_id = data.get('renter_id')
    apartment_id = data.get('apartment_id')
    reservation_order_id = data.get('reservation_order_id')

    updated_review_dto = ReviewsService.update_review(review_id, description, point, renter_id, apartment_id,
                                                      reservation_order_id)
    if updated_review_dto:
        return jsonify(updated_review_dto.to_dict())
    else:
        return jsonify({'error': 'Review not found'}), 404


@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    deleted_review_dto = ReviewsService.delete_review(review_id)
    if deleted_review_dto:
        return jsonify(deleted_review_dto.to_dict())
    else:
        return jsonify({'error': 'Review not found'}), 404
