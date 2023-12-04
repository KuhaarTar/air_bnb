from app import db
from app.models import ApartmentPhoto


class ApartmentPhotoDAO:
    @staticmethod
    def create_apartment_photo(photo_url, description, apartment_id):
        apartment_photo = ApartmentPhoto(
            photo_url=photo_url,
            description=description,
            apartment_id=apartment_id
        )
        db.session.add(apartment_photo)
        db.session.commit()
        return apartment_photo

    @staticmethod
    def get_apartment_photos():
        return ApartmentPhoto.query.all()

    @staticmethod
    def get_apartment_photo_by_id(id):
        return ApartmentPhoto.query.get(id)

    @staticmethod
    def get_apartment_photos_new(apartment_id):
        return ApartmentPhoto.query.filter_by(apartment_id=apartment_id).all()

    @staticmethod
    def update_apartment_photo(photo_id, photo_url=None, description=None, apartment_id=None):
        apartment_photo = ApartmentPhoto.query.get(photo_id)

        if apartment_photo:
            if photo_url is not None:
                apartment_photo.photo_url = photo_url
            if description is not None:
                apartment_photo.description = description
            if apartment_id is not None:
                apartment_photo.apartment_id = apartment_id

            db.session.commit()

        return apartment_photo

    @staticmethod
    def delete_apartment_photo(photo_id):
        apartment_photo = ApartmentPhoto.query.get(photo_id)
        if apartment_photo:
            db.session.delete(apartment_photo)
            db.session.commit()
        return apartment_photo
