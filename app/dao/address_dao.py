from app import db
from app.models import Address


class AddressDAO:
    @staticmethod
    def create_address(city_name, country_name, geo_location, street, building, flat=None):
        address = Address(
            city_name=city_name,
            country_name=country_name,
            geo_location=geo_location,
            street=street,
            building=building,
            flat=flat
        )
        db.session.add(address)
        db.session.commit()
        return address

    @staticmethod
    def get_addresses():
        return Address.query.all()

    @staticmethod
    def get_address_by_id(address_id):
        return Address.query.get(address_id)

    @staticmethod
    def update_address(address_id, city_name=None, country_name=None, geo_location=None, street=None,
                       building=None, flat=None):
        address = AddressDAO.get_address_by_id(address_id)

        if address:
            if city_name:
                address.city_name = city_name
            if country_name:
                address.country_name = country_name
            if geo_location:
                address.geo_location = geo_location
            if street:
                address.street = street
            if building:
                address.building = building
            if flat:
                address.flat = flat

            db.session.commit()

        return address

    @staticmethod
    def delete_address(address_id):
        address = AddressDAO.get_address_by_id(address_id)

        if address:
            db.session.delete(address)
            db.session.commit()

        return address
