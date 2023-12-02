from app import db
from app.models.apartment import Apartment


class ApartmentDAO:
    @staticmethod
    def create_apartment(area_of_territory, enable_to_reserve, cost_per_hour, lessor_id, address_id, rating_id):
        apartment = Apartment(
            area_of_territory=area_of_territory,
            enable_to_reserve=enable_to_reserve,
            cost_per_hour=cost_per_hour,
            lessor_id=lessor_id,
            address_id=address_id,
            rating_id=rating_id
        )
        db.session.add(apartment)
        db.session.commit()
        return apartment

    @staticmethod
    def get_apartments():
        return Apartment.query.all()

    @staticmethod
    def get_apartment_by_id(apartment_id):
        return Apartment.query.get(apartment_id)

    @staticmethod
    def update_apartment(apartment_id, area_of_territory=None, enable_to_reserve=None, cost_per_hour=None,
                         lessor_id=None, address_id=None, rating_id=None):
        apartment = Apartment.get_apartment_by_id(apartment_id)

        if apartment:
            if area_of_territory:
                apartment.area_of_territory = area_of_territory
            if enable_to_reserve is not None:
                apartment.enable_to_reserve = enable_to_reserve
            if cost_per_hour:
                apartment.cost_per_hour = cost_per_hour
            if lessor_id:
                apartment.lessor_id = lessor_id
            if address_id:
                apartment.address_id = address_id
            if rating_id:
                apartment.rating_id = rating_id

            db.session.commit()

        return apartment

    @staticmethod
    def delete_apartment(apartment_id):
        apartment = Apartment.get_apartment_by_id(apartment_id)

        if apartment:
            db.session.delete(apartment)
            db.session.commit()

        return apartment
