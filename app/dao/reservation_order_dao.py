from app import db
from app.models import ReservationOrder


class ReservationOrderDAO:
    @staticmethod
    def create_reservation_order(is_confirmed, start_date, end_date, apartment, renter):
        reservation_order = ReservationOrder(
            is_confirmed=is_confirmed,
            start_date=start_date,
            end_date=end_date,
            apartment=apartment,
            renter=renter
        )
        db.session.add(reservation_order)
        db.session.commit()
        return reservation_order

    @staticmethod
    def get_reservation_orders():
        return ReservationOrder.query.all()

    @staticmethod
    def get_reservation_order_by_id(reservation_order_id):
        return ReservationOrder.query.get(reservation_order_id)

    @staticmethod
    def update_reservation_order(reservation_order_id, is_confirmed=None, start_date=None, end_date=None,
                                 apartment=None, renter=None):
        reservation_order = ReservationOrderDAO.get_reservation_order_by_id(reservation_order_id)

        if reservation_order:
            if is_confirmed is not None:
                reservation_order.is_confirmed = is_confirmed
            if start_date:
                reservation_order.start_date = start_date
            if end_date:
                reservation_order.end_date = end_date
            if apartment:
                reservation_order.apartment = apartment
            if renter:
                reservation_order.renter = renter

            db.session.commit()

        return reservation_order

    @staticmethod
    def delete_reservation_order(reservation_order_id):
        reservation_order = ReservationOrderDAO.get_reservation_order_by_id(reservation_order_id)

        if reservation_order:
            db.session.delete(reservation_order)
            db.session.commit()

        return reservation_order
