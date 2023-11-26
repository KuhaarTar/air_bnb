from app.dao.renter_dao import RenterDAO
from app.dto import RenterDTO


class RenterService:
    @staticmethod
    def create_renter(first_name, last_name, email, phone):
        renter = RenterDAO.create_renter(first_name, last_name, email, phone)
        return RenterDTO(renter.id, renter.first_name, renter.last_name, renter.email, renter.phone)

    @staticmethod
    def get_renters():
        renters_list = RenterDAO.get_renters()
        return [RenterDTO(renter.id, renter.first_name, renter.last_name, renter.email, renter.phone)
                for renter in renters_list]

    @staticmethod
    def get_renter_by_id(renter_id):
        renter = RenterDAO.get_renter_by_id(renter_id)
        if renter:
            return RenterDTO(renter.id, renter.first_name, renter.last_name, renter.email, renter.phone)
        else:
            return None

    @staticmethod
    def update_renter(renter_id, first_name=None, last_name=None, email=None, phone=None):
        updated_renter = RenterDAO.update_renter(renter_id, first_name, last_name, email, phone)
        if updated_renter:
            return RenterDTO(updated_renter.id, updated_renter.first_name, updated_renter.last_name,
                             updated_renter.email, updated_renter.phone)
        else:
            return None

    @staticmethod
    def delete_renter(renter_id):
        deleted_renter = RenterDAO.delete_renter(renter_id)
        if deleted_renter:
            return RenterDTO(deleted_renter.id, deleted_renter.first_name, deleted_renter.last_name,
                             deleted_renter.email, deleted_renter.phone)
        else:
            return None
