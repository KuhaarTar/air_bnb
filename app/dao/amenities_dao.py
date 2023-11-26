from app import db
from app.models import Amenities


class AmenitiesDAO:
    @staticmethod
    def create_amenities(name, description, category):
        amenities = Amenities(
            name=name,
            description=description,
            category=category
        )
        db.session.add(amenities)
        db.session.commit()
        return amenities

    @staticmethod
    def get_amenities():
        return Amenities.query.all()

    @staticmethod
    def get_amenities_by_id(amenities_id):
        return Amenities.query.get(amenities_id)

    @staticmethod
    def update_amenities(amenities_id, name=None, description=None, category=None):
        amenities = AmenitiesDAO.get_amenities_by_id(amenities_id)

        if amenities:
            if name:
                amenities.name = name
            if description:
                amenities.description = description
            if category:
                amenities.category = category

            db.session.commit()

        return amenities

    @staticmethod
    def delete_amenities(amenities_id):
        amenities = AmenitiesDAO.get_amenities_by_id(amenities_id)

        if amenities:
            db.session.delete(amenities)
            db.session.commit()

        return amenities
