from app.dao.address_dao import AddressDAO
from app.dto import AddressDTO


class AddressService:
    @staticmethod
    def create_address(city_name, country_name, geo_location, street, building, flat=None):
        address = AddressDAO.create_address(city_name, country_name, geo_location, street, building, flat)
        return AddressDTO(address.id, address.city_name, address.country_name, address.geo_location,
                          address.street, address.building, address.flat)

    @staticmethod
    def get_addresses():
        addresses = AddressDAO.get_addresses()
        return [AddressDTO(address.id, address.city_name, address.country_name, address.geo_location,
                           address.street, address.building, address.flat) for address in addresses]

    @staticmethod
    def get_address_by_id(address_id):
        address = AddressDAO.get_address_by_id(address_id)
        if address:
            return AddressDTO(address.id, address.city_name, address.country_name, address.geo_location,
                              address.street, address.building, address.flat)
        return None

    @staticmethod
    def update_address(address_id, city_name=None, country_name=None, geo_location=None, street=None,
                       building=None, flat=None):
        address = AddressDAO.update_address(address_id, city_name, country_name, geo_location,
                                            street, building, flat)
        if address:
            return AddressDTO(address.id, address.city_name, address.country_name, address.geo_location,
                              address.street, address.building, address.flat)
        return None

    @staticmethod
    def delete_address(address_id):
        address = AddressDAO.delete_address(address_id)
        if address:
            return AddressDTO(address.id, address.city_name, address.country_name, address.geo_location,
                              address.street, address.building, address.flat)
        return None
