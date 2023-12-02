from flask import jsonify, request
from app import app
from app.services.address_service import AddressService


@app.route('/addresses', methods=['GET'])
def get_addresses():
    addresses = AddressService.get_addresses()
    addresses_list = [address.to_dict() for address in addresses]
    return jsonify({'addresses': addresses_list})


@app.route('/addresses/<int:address_id>', methods=['GET'])
def get_address_by_id(address_id):
    address = AddressService.get_address_by_id(address_id)
    if address:
        return jsonify(address.to_dict())
    else:
        return jsonify({'message': 'Address not found'}), 404


@app.route('/addresses', methods=['POST'])
def create_address():
    data = request.get_json()
    city_name = data.get('city_name')
    country_name = data.get('country_name')
    geo_location = data.get('geo_location')
    street = data.get('street')
    building = data.get('building')
    flat = data.get('flat')

    if not city_name or not country_name or not geo_location or not street or not building:
        return jsonify({'message': 'Incomplete data provided'}), 400

    address = AddressService.create_address(city_name, country_name, geo_location, street, building, flat)
    return jsonify(address.to_dict()), 201


@app.route('/addresses/<int:address_id>', methods=['PUT'])
def update_address(address_id):
    data = request.get_json()
    city_name = data.get('city_name')
    country_name = data.get('country_name')
    geo_location = data.get('geo_location')
    street = data.get('street')
    building = data.get('building')
    flat = data.get('flat')

    updated_address = AddressService.update_address(address_id, city_name, country_name, geo_location,
                                                    street, building, flat)
    if updated_address:
        return jsonify(updated_address.to_dict())
    else:
        return jsonify({'message': 'Address not found'}), 404


@app.route('/addresses/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    deleted_address = AddressService.delete_address(address_id)
    if deleted_address:
        return jsonify(deleted_address.to_dict())
    else:
        return jsonify({'message': 'Address not found'}), 404
