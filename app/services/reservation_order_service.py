from app.dao.reservation_order_dao import ReservationOrderDAO
from app.dto import ReservationOrderDTO


class ReservationOrderService:
    @staticmethod
    def create_reservation_order(is_confirmed, start_date, end_date, apartment_id, renter_id):
        reservation_order = ReservationOrderDAO.create_reservation_order(is_confirmed, start_date, end_date,
                                                                        apartment_id, renter_id)
        return ReservationOrderDTO(reservation_order.id, reservation_order.is_confirmed,
                                   reservation_order.start_date, reservation_order.end_date,
                                   reservation_order.apartment, reservation_order.renter)

    @staticmethod
    def get_reservation_orders():
        reservation_orders_list = ReservationOrderDAO.get_reservation_orders()
        return [ReservationOrderDTO(reservation_order.id, reservation_order.is_confirmed,
                                    reservation_order.start_date, reservation_order.end_date,
                                    reservation_order.apartment, reservation_order.renter)
                for reservation_order in reservation_orders_list]

    @staticmethod
    def get_reservation_order_by_id(reservation_order_id):
        reservation_order = ReservationOrderDAO.get_reservation_order_by_id(reservation_order_id)
        if reservation_order:
            return ReservationOrderDTO(reservation_order.id, reservation_order.is_confirmed,
                                       reservation_order.start_date, reservation_order.end_date,
                                       reservation_order.apartment, reservation_order.renter)
        else:
            return None

    @staticmethod
    def update_reservation_order(reservation_order_id, is_confirmed=None, start_date=None, end_date=None,
                                 apartment_id=None, renter_id=None):
        updated_reservation_order = ReservationOrderDAO.update_reservation_order(reservation_order_id,
                                                                                  is_confirmed, start_date, end_date,
                                                                                  apartment_id, renter_id)
        if updated_reservation_order:
            return ReservationOrderDTO(updated_reservation_order.id, updated_reservation_order.is_confirmed,
                                       updated_reservation_order.start_date, updated_reservation_order.end_date,
                                       updated_reservation_order.apartment, updated_reservation_order.renter)
        else:
            return None

    @staticmethod
    def delete_reservation_order(reservation_order_id):
        deleted_reservation_order = ReservationOrderDAO.delete_reservation_order(reservation_order_id)
        if deleted_reservation_order:
            return ReservationOrderDTO(deleted_reservation_order.id, deleted_reservation_order.is_confirmed,
                                       deleted_reservation_order.start_date, deleted_reservation_order.end_date,
                                       deleted_reservation_order.apartment, deleted_reservation_order.renter)
        else:
            return None
