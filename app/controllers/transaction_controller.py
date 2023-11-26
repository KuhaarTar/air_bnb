from flask import jsonify, request

from app import app
from app.services.transaction_service import TransactionService


@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = TransactionService.get_transactions()
    return jsonify([transaction.to_dict() for transaction in transactions])


@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction_by_id(transaction_id):
    transaction = TransactionService.get_transaction_by_id(transaction_id)
    if transaction:
        return jsonify(transaction.to_dict())
    else:
        return jsonify({'error': 'Transaction not found'}), 404


@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    transaction_type = data.get('transaction_type')
    amount = data.get('amount')
    reservation_order_id = data.get('reservation_order_id')
    apartment_id = data.get('apartment_id')
    renter_id = data.get('renter_id')

    if not all([transaction_type, amount, reservation_order_id, apartment_id, renter_id]):
        return jsonify({'error': 'Missing required fields'}), 400

    transaction = TransactionService.create_transaction(transaction_type, amount, reservation_order_id,
                                                        apartment_id, renter_id)
    return jsonify(transaction.to_dict()), 201


@app.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    data = request.get_json()
    transaction_type = data.get('transaction_type')
    amount = data.get('amount')
    reservation_order_id = data.get('reservation_order_id')
    apartment_id = data.get('apartment_id')
    renter_id = data.get('renter_id')

    updated_transaction = TransactionService.update_transaction(transaction_id, transaction_type, amount,
                                                                reservation_order_id, apartment_id, renter_id)
    if updated_transaction:
        return jsonify(updated_transaction.to_dict())
    else:
        return jsonify({'error': 'Transaction not found'}), 404


@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    deleted_transaction = TransactionService.delete_transaction(transaction_id)
    if deleted_transaction:
        return jsonify(deleted_transaction.to_dict())
    else:
        return jsonify({'error': 'Transaction not found'}), 404
