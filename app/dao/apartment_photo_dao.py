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
    def delete_apartment_photo(photo_url):
        apartment_photo = ApartmentPhoto.query.filter_by(photo_url=photo_url).first()
        if apartment_photo:
            db.session.delete(apartment_photo)
            db.session.commit()
        return apartment_photo
