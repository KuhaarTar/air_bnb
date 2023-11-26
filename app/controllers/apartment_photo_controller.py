from flask import jsonify, request
from app.services.apartment_photo_service import ApartmentPhotoService
from app import app


@app.route('/apartment-photos', methods=['POST'])
def create_apartment_photo():
    data = request.json
    photo_url = data.get('photo_url')
    description = data.get('description')
    apartment_id = data.get('apartment_id')

    if not photo_url or not apartment_id:
        return jsonify({'error': 'Photo URL and Apartment ID are required'}), 400

    apartment_photo_dto = ApartmentPhotoService.create_apartment_photo(photo_url, description, apartment_id)
    return jsonify(apartment_photo_dto.to_dict()), 201


@app.route('/apartment-photos', methods=['GET'])
def get_apartment_photos():
    photos_list = ApartmentPhotoService.get_apartment_photos()
    return jsonify([photo.to_dict() for photo in photos_list])


@app.route('/apartment-photos/<int:photo_id>', methods=['GET'])
def get_apartment_photo_by_id(photo_id):
    photo_dto = ApartmentPhotoService.get_apartment_photo_by_id(photo_id)
    if photo_dto:
        return jsonify(photo_dto.to_dict())
    else:
        return jsonify({'error': 'Apartment Photo not found'}), 404


@app.route('/apartment-photos/<int:photo_id>', methods=['PUT'])
def update_apartment_photo(photo_id):
    data = request.json
    photo_url = data.get('photo_url')
    description = data.get('description')
    apartment_id = data.get('apartment_id')

    updated_photo_dto = ApartmentPhotoService.update_apartment_photo(photo_id, photo_url, description, apartment_id)
    if updated_photo_dto:
        return jsonify(updated_photo_dto.to_dict())
    else:
        return jsonify({'error': 'Apartment Photo not found'}), 404


@app.route('/apartment-photos/<int:photo_id>', methods=['DELETE'])
def delete_apartment_photo(photo_id):
    deleted_photo_dto = ApartmentPhotoService.delete_apartment_photo(photo_id)
    if deleted_photo_dto:
        return jsonify(deleted_photo_dto.to_dict())
    else:
        return jsonify({'error': 'Apartment Photo not found'}), 404
