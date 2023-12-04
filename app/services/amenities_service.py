from app.dao.amenities_dao import AmenitiesDAO
from app.dao.apartment_has_amenities_dao import ApartmentHasAmenitiesDAO
from app.dto import AmenitiesDTO


class AmenitiesService:
    @staticmethod
    def create_amenities(name, description, category):
        amenities = AmenitiesDAO.create_amenities(name, description, category)
        return AmenitiesDTO(amenities.amenities_id, amenities.name, amenities.description, amenities.category)

    @staticmethod
    def get_amenities():
        amenities_list = AmenitiesDAO.get_amenities()
        return [AmenitiesDTO(amenities.amenities_id, amenities.name, amenities.description, amenities.category)
                for amenities in amenities_list]

    @staticmethod
    def get_amenities_by_id(amenities_id):
        amenities = AmenitiesDAO.get_amenities_by_id(amenities_id)
        if amenities:
            return AmenitiesDTO(amenities.amenities_id, amenities.name, amenities.description, amenities.category)
        else:
            return None

    @staticmethod
    def update_amenities(amenities_id, name=None, description=None, category=None):
        updated_amenities = AmenitiesDAO.update_amenities(amenities_id, name, description, category)
        if updated_amenities:
            return AmenitiesDTO(updated_amenities.amenities_id, updated_amenities.name,
                                updated_amenities.description, updated_amenities.category)
        else:
            return None

    @staticmethod
    def delete_amenities(amenities_id):
        ApartmentHasAmenitiesDAO.remove_amenities_by_id(amenities_id)
        deleted_amenities = AmenitiesDAO.delete_amenities(amenities_id)
        if deleted_amenities:
            return AmenitiesDTO(deleted_amenities.amenities_id, deleted_amenities.name,
                                deleted_amenities.description, deleted_amenities.category)
        else:
            return None
