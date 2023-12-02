from flask import  jsonify, request

from app import app
from app.services.apartment_rating_service import ApartmentRatingService


@app.route('/apartment-ratings', methods=['GET'])
def get_apartment_ratings():
    ratings = ApartmentRatingService.get_apartment_ratings()
    return jsonify([rating.to_dict() for rating in ratings])


@app.route('/apartment-ratings/<int:rating_id>', methods=['GET'])
def get_apartment_rating_by_id(rating_id):
    rating = ApartmentRatingService.get_apartment_rating_by_id(rating_id)
    if rating:
        return jsonify(rating.to_dict())
    else:
        return jsonify({'error': 'Apartment Rating not found'}), 404


@app.route('/apartment-ratings', methods=['POST'])
def create_apartment_rating():
    data = request.get_json()
    count_of_reviews = data.get('count_of_reviews')
    avg_point = data.get('avg_point')
    time_created = data.get('time_created')
    time_modified = data.get('time_modified')

    if not all([count_of_reviews, avg_point, time_created, time_modified]):
        return jsonify({'error': 'Missing required fields'}), 400

    rating = ApartmentRatingService.create_apartment_rating(count_of_reviews, avg_point, time_created, time_modified)
    return jsonify(rating.to_dict()), 201


@app.route('/apartment-ratings/<int:rating_id>', methods=['PUT'])
def update_apartment_rating(rating_id):
    data = request.get_json()
    count_of_reviews = data.get('count_of_reviews')
    avg_point = data.get('avg_point')
    time_created = data.get('time_created')
    time_modified = data.get('time_modified')

    updated_rating = ApartmentRatingService.update_apartment_rating(rating_id, count_of_reviews, avg_point,
                                                                    time_created, time_modified)
    if updated_rating:
        return jsonify(updated_rating.to_dict())
    else:
        return jsonify({'error': 'Apartment Rating not found'}), 404


@app.route('/apartment-ratings/<int:rating_id>', methods=['DELETE'])
def delete_apartment_rating(rating_id):
    deleted_rating = ApartmentRatingService.delete_apartment_rating(rating_id)
    if deleted_rating:
        return jsonify(deleted_rating.to_dict())
    else:
        return jsonify({'error': 'Apartment Rating not found'}), 404
