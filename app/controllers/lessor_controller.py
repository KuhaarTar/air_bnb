from flask import jsonify, request

from app import app
from app.services.lessor_service import LessorService


@app.route('/lessors', methods=['GET'])
def get_lessors():
    lessors = LessorService.get_lessors()
    return jsonify({'lessors': [lessor.to_dict() for lessor in lessors]})


@app.route('/lessors/<int:lessor_id>', methods=['GET'])
def get_lessor_by_id(lessor_id):
    lessor = LessorService.get_lessor_by_id(lessor_id)

    if lessor:
        return jsonify(lessor.to_dict())
    else:
        return jsonify({'message': 'Lessor not found'}), 404


@app.route('/lessors', methods=['POST'])
def create_lessor():
    data = request.get_json()
    lessor = LessorService.create_lessor(**data)
    return jsonify(lessor.to_dict()), 201


@app.route('/lessors/<int:lessor_id>', methods=['PUT'])
def update_lessor(lessor_id):
    data = request.get_json()
    updated_lessor = LessorService.update_lessor(lessor_id, **data)

    if updated_lessor:
        return jsonify(updated_lessor.to_dict())
    else:
        return jsonify({'message': 'Lessor not found'}), 404


@app.route('/lessors/<int:lessor_id>', methods=['DELETE'])
def delete_lessor(lessor_id):
    deleted_lessor = LessorService.delete_lessor(lessor_id)

    if deleted_lessor:
        return jsonify(deleted_lessor.to_dict())
    else:
        return jsonify({'message': 'Lessor not found'}), 404
