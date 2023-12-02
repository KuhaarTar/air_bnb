from flask import jsonify, request
from app import app
from app.services.apartmnet_service import ApartmentService


@app.route('/apartments', methods=['GET'])
def get_apartments():
    apartments = ApartmentService.get_apartments()
    apartments_list = [apartment.to_dict() for apartment in apartments]
    return jsonify({'apartments': apartments_list})


@app.route('/apartments/<int:apartment_id>', methods=['GET'])
def get_apartment_by_id(apartment_id):
    apartment = ApartmentService.get_apartment_by_id(apartment_id)
    if apartment:
        return jsonify(apartment.to_dict())
    else:
        return jsonify({'message': 'Apartment not found'}), 404


@app.route('/apartments', methods=['POST'])
def create_apartment():
    data = request.get_json()
    area_of_territory = data.get('area_of_territory')
    enable_to_reserve = data.get('enable_to_reserve')
    cost_per_hour = data.get('cost_per_hour')
    lessor_id = data.get('lessor_id')
    address_id = data.get('address_id')
    rating_id = data.get('rating_id')

    if not area_of_territory or not enable_to_reserve or not cost_per_hour or not lessor_id or not address_id or not rating_id:
        return jsonify({'message': 'Incomplete data provided'}), 400

    apartment = ApartmentService.create_apartment(area_of_territory, enable_to_reserve, cost_per_hour,
                                                  lessor_id, address_id, rating_id)
    return jsonify(apartment.to_dict()), 201


@app.route('/apartments/<int:apartment_id>', methods=['PUT'])
def update_apartment(apartment_id):
    data = request.get_json()
    area_of_territory = data.get('area_of_territory')
    enable_to_reserve = data.get('enable_to_reserve')
    cost_per_hour = data.get('cost_per_hour')
    lessor_id = data.get('lessor_id')
    address_id = data.get('address_id')
    rating_id = data.get('rating_id')

    updated_apartment = ApartmentService.update_apartment(apartment_id, area_of_territory, enable_to_reserve,
                                                          cost_per_hour, lessor_id, address_id, rating_id)
    if updated_apartment:
        return jsonify(updated_apartment.to_dict())
    else:
        return jsonify({'message': 'Apartment not found'}), 404


@app.route('/apartments/<int:apartment_id>', methods=['DELETE'])
def delete_apartment(apartment_id):
    deleted_apartment = ApartmentService.delete_apartment(apartment_id)
    if deleted_apartment:
        return jsonify(deleted_apartment.to_dict())
    else:
        return jsonify({'message': 'Apartment not found'})
