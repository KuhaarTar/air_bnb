from app.dao.apartment_photo_dao import ApartmentPhotoDAO
from app.dto import ApartmentPhotoDTO


class ApartmentPhotoService:
    @staticmethod
    def create_apartment_photo(photo_url, description, apartment_id):
        apartment_photo = ApartmentPhotoDAO.create_apartment_photo(photo_url, description, apartment_id)
        return ApartmentPhotoDTO(apartment_photo.id, apartment_photo.photo_url,
                                 apartment_photo.description, apartment_photo.apartment_id)

    @staticmethod
    def get_apartment_photos():
        apartment_photos_list = ApartmentPhotoDAO.get_apartment_photos()
        return [ApartmentPhotoDTO(photo.id, photo.photo_url, photo.description, photo.apartment_id)
                for photo in apartment_photos_list]

    @staticmethod
    def get_apartment_photo_by_id(photo_id):
        photo = ApartmentPhotoDAO.get_apartment_photo_by_id(photo_id)
        if photo:
            return ApartmentPhotoDTO(photo.id, photo.photo_url, photo.description, photo.apartment_id)
        else:
            return None

    @staticmethod
    def update_apartment_photo(photo_id, photo_url=None, description=None, apartment_id=None):
        updated_photo = ApartmentPhotoDAO.update_apartment_photo(photo_id, photo_url, description, apartment_id)
        if updated_photo:
            return ApartmentPhotoDTO(updated_photo.id, updated_photo.photo_url,
                                     updated_photo.description, updated_photo.apartment_id)
        else:
            return None

    @staticmethod
    def delete_apartment_photo(photo_id):
        deleted_photo = ApartmentPhotoDAO.delete_apartment_photo(photo_id)
        if deleted_photo:
            return ApartmentPhotoDTO(deleted_photo.id, deleted_photo.photo_url,
                                     deleted_photo.description, deleted_photo.apartment_id)
        else:
            return None
