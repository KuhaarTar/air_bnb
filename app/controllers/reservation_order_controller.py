from flask import jsonify, request
from app.services.reservation_order_service import ReservationOrderService
from app import app


@app.route('/reservation_orders', methods=['POST'])
def create_reservation_order():
    data = request.json
    is_confirmed = data.get('is_confirmed')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    apartment_id = data.get('apartment_id')
    renter_id = data.get('renter_id')

    if not is_confirmed or not start_date or not end_date or not apartment_id or not renter_id:
        return jsonify({'error': 'is_confirmed, start_date, end_date, apartment_id, and renter_id are required'}), 400

    reservation_order_dto = ReservationOrderService.create_reservation_order(is_confirmed, start_date, end_date,
                                                                             apartment_id, renter_id)
    return jsonify(reservation_order_dto.to_dict()), 201


@app.route('/reservation_orders', methods=['GET'])
def get_reservation_orders():
    reservation_orders_list = ReservationOrderService.get_reservation_orders()
    return jsonify([reservation_order.to_dict() for reservation_order in reservation_orders_list])


@app.route('/reservation_orders/<int:reservation_order_id>', methods=['GET'])
def get_reservation_order_by_id(reservation_order_id):
    reservation_order_dto = ReservationOrderService.get_reservation_order_by_id(reservation_order_id)
    if reservation_order_dto:
        return jsonify(reservation_order_dto.to_dict())
    else:
        return jsonify({'error': 'Reservation Order not found'}), 404


@app.route('/reservation_orders/<int:reservation_order_id>', methods=['PUT'])
def update_reservation_order(reservation_order_id):
    data = request.json
    is_confirmed = data.get('is_confirmed')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    apartment_id = data.get('apartment_id')
    renter_id = data.get('renter_id')

    updated_reservation_order_dto = ReservationOrderService.update_reservation_order(reservation_order_id,
                                                                                     is_confirmed, start_date,
                                                                                     end_date, apartment_id, renter_id)
    if updated_reservation_order_dto:
        return jsonify(updated_reservation_order_dto.to_dict())
    else:
        return jsonify({'error': 'Reservation Order not found'}), 404


@app.route('/reservation_orders/<int:reservation_order_id>', methods=['DELETE'])
def delete_reservation_order(reservation_order_id):
    deleted_reservation_order_dto = ReservationOrderService.delete_reservation_order(reservation_order_id)
    if deleted_reservation_order_dto:
        return jsonify(deleted_reservation_order_dto.to_dict())
    else:
        return jsonify({'error': 'Reservation Order not found'}), 404
