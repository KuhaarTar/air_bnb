from flask import jsonify, request
from app.services.renter_service import RenterService
from app import app


@app.route('/renters', methods=['POST'])
def create_renter():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')

    if not first_name or not last_name or not email or not phone:
        return jsonify({'error': 'First Name, Last Name, Email, and Phone are required'}), 400

    renter_dto = RenterService.create_renter(first_name, last_name, email, phone)
    return jsonify(renter_dto.to_dict()), 201


@app.route('/renters', methods=['GET'])
def get_renters():
    renters_list = RenterService.get_renters()
    return jsonify([renter.to_dict() for renter in renters_list])


@app.route('/renters/<int:renter_id>', methods=['GET'])
def get_renter_by_id(renter_id):
    renter_dto = RenterService.get_renter_by_id(renter_id)
    if renter_dto:
        return jsonify(renter_dto.to_dict())
    else:
        return jsonify({'error': 'Renter not found'}), 404


@app.route('/renters/<int:renter_id>', methods=['PUT'])
def update_renter(renter_id):
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')

    updated_renter_dto = RenterService.update_renter(renter_id, first_name, last_name, email, phone)
    if updated_renter_dto:
        return jsonify(updated_renter_dto.to_dict())
    else:
        return jsonify({'error': 'Renter not found'}), 404


@app.route('/renters/<int:renter_id>', methods=['DELETE'])
def delete_renter(renter_id):
    deleted_renter_dto = RenterService.delete_renter(renter_id)
    if deleted_renter_dto:
        return jsonify(deleted_renter_dto.to_dict())
    else:
        return jsonify({'error': 'Renter not found'}), 404
