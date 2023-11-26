from app.dao.apartmnet_dao import ApartmentDAO
from app.dto import ApartmentDTO


class ApartmentService:
    @staticmethod
    def create_apartment(area_of_territory, enable_to_reserve, cost_per_hour, lessor_id, address_id, rating_id):
        apartment = ApartmentDAO.create_apartment(area_of_territory, enable_to_reserve, cost_per_hour,
                                                  lessor_id, address_id, rating_id)
        return ApartmentDTO(apartment.id, apartment.area_of_territory, apartment.enable_to_reserve,
                            apartment.cost_per_hour, apartment.lessor, apartment.address, apartment.rating)

    @staticmethod
    def get_apartments():
        apartments = ApartmentDAO.get_apartments()
        return [ApartmentDTO(apartment.id, apartment.area_of_territory, apartment.enable_to_reserve,
                             apartment.cost_per_hour, apartment.lessor, apartment.address, apartment.rating)
                for apartment in apartments]

    @staticmethod
    def get_apartment_by_id(apartment_id):
        apartment = ApartmentDAO.get_apartment_by_id(apartment_id)
        if apartment:
            return ApartmentDTO(apartment.id, apartment.area_of_territory, apartment.enable_to_reserve,
                                apartment.cost_per_hour, apartment.lessor, apartment.address, apartment.rating)
        else:
            return None

    @staticmethod
    def update_apartment(apartment_id, area_of_territory=None, enable_to_reserve=None, cost_per_hour=None,
                         lessor_id=None, address_id=None, rating_id=None):
        updated_apartment = ApartmentDAO.update_apartment(apartment_id, area_of_territory, enable_to_reserve,
                                                          cost_per_hour, lessor_id, address_id, rating_id)
        if updated_apartment:
            return ApartmentDTO(updated_apartment.id, updated_apartment.area_of_territory,
                                updated_apartment.enable_to_reserve, updated_apartment.cost_per_hour,
                                updated_apartment.lessor, updated_apartment.address, updated_apartment.rating)
        else:
            return None

    @staticmethod
    def delete_apartment(apartment_id):
        deleted_apartment = ApartmentDAO.delete_apartment(apartment_id)
        if deleted_apartment:
            return ApartmentDTO(deleted_apartment.id, deleted_apartment.area_of_territory,
                                deleted_apartment.enable_to_reserve, deleted_apartment.cost_per_hour,
                                deleted_apartment.lessor, deleted_apartment.address, deleted_apartment.rating)
        else:
            return None
