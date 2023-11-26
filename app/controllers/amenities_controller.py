from flask import Blueprint, jsonify, request

from app import app
from app.services.amenities_service import AmenitiesService

@app.route('/amenities', methods=['POST'])
def create_amenities():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    category = data.get('category')

    if not name or not category:
        return jsonify({'error': 'Name and Category are required'}), 400

    amenities_dto = AmenitiesService.create_amenities(name, description, category)
    return jsonify(amenities_dto.to_dict()), 201


@app.route('/amenities', methods=['GET'])
def get_amenities():
    amenities_list = AmenitiesService.get_amenities()
    return jsonify([amenities.to_dict() for amenities in amenities_list])


@app.route('/amenities/<int:amenities_id>', methods=['GET'])
def get_amenities_by_id(amenities_id):
    amenities_dto = AmenitiesService.get_amenities_by_id(amenities_id)
    if amenities_dto:
        return jsonify(amenities_dto.to_dict())
    else:
        return jsonify({'error': 'Amenities not found'}), 404


@app.route('/amenities/<int:amenities_id>', methods=['PUT'])
def update_amenities(amenities_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    category = data.get('category')

    updated_amenities_dto = AmenitiesService.update_amenities(amenities_id, name, description, category)
    if updated_amenities_dto:
        return jsonify(updated_amenities_dto.to_dict())
    else:
        return jsonify({'error': 'Amenities not found'}), 404


@app.route('/amenities/<int:amenities_id>', methods=['DELETE'])
def delete_amenities(amenities_id):
    deleted_amenities_dto = AmenitiesService.delete_amenities(amenities_id)
    if deleted_amenities_dto:
        return jsonify(deleted_amenities_dto.to_dict())
    else:
        return jsonify({'error': 'Amenities not found'}), 404
