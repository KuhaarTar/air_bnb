from app import db
from app.models import ApartmentHasAmenities


class ApartmentHasAmenitiesDAO:
    @staticmethod
    def add_amenities_to_apartment(amenities_id, apartment_id):
        apartment_has_amenities = ApartmentHasAmenities(amenities_id=amenities_id, apartment_id=apartment_id)
        db.session.add(apartment_has_amenities)
        db.session.commit()
        return apartment_has_amenities

    @staticmethod
    def get_amenities_for_apartment(apartment_id):
        return ApartmentHasAmenities.query.filter_by(apartment_id=apartment_id).all()

    @staticmethod
    def remove_amenities_from_apartment(amenities_id, apartment_id):
        apartment_has_amenities = ApartmentHasAmenities.query.get((amenities_id, apartment_id))

        if apartment_has_amenities:
            db.session.delete(apartment_has_amenities)
            db.session.commit()

        return apartment_has_amenities
