class LessorDTO:
    def __init__(self, id, email, phone, first_name, last_name):
        self.id = id
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'phone': self.phone,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


class AddressDTO:
    def __init__(self, id, city_name, country_name, geo_location, street, building, flat):
        self.id = id
        self.city_name = city_name
        self.country_name = country_name
        self.geo_location = geo_location
        self.street = street
        self.building = building
        self.flat = flat

    def to_dict(self):
        return {
            'id': self.id,
            'city_name': self.city_name,
            'country_name': self.country_name,
            'geo_location': self.geo_location,
            'street': self.street,
            'building': self.building,
            'flat': self.flat
        }


class ApartmentDTO:
    def __init__(self, id, area_of_territory, enable_to_reserve, cost_per_hour, lessor, address, rating):
        self.id = id
        self.area_of_territory = area_of_territory
        self.enable_to_reserve = enable_to_reserve
        self.cost_per_hour = cost_per_hour
        self.lessor = lessor
        self.address = address
        self.rating = rating

    def to_dict(self):
        return {
            'id': self.id,
            'area_of_territory': self.area_of_territory,
            'enable_to_reserve': self.enable_to_reserve,
            'cost_per_hour': self.cost_per_hour,
            'lessor': self.lessor.to_dict(),
            'address': self.address.to_dict(),
            'rating': self.rating.to_dict()
        }


class AmenitiesDTO:
    def __init__(self, amenities_id, name, description, category):
        self.amenities_id = amenities_id
        self.name = name
        self.description = description
        self.category = category

    def to_dict(self):
        return {
            'amenities_id': self.amenities_id,
            'name': self.name,
            'description': self.description,
            'category': self.category
        }


class ApartmentPhotoDTO:
    def __init__(self, id, photo_url, description, apartment_id):
        self.id = id
        self.photo_url = photo_url
        self.description = description
        self.apartment_id = apartment_id

    def to_dict(self):
        return {
            'id': self.id,
            'photo_url': self.photo_url,
            'description': self.description,
            'apartment_id': self.apartment_id
        }


class RenterDTO:
    def __init__(self, id, first_name, last_name, email, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone
        }


class ReservationOrderDTO:
    def __init__(self, id, is_confirmed, start_date, end_date, apartment, renter):
        self.id = id
        self.is_confirmed = is_confirmed
        self.start_date = start_date
        self.end_date = end_date
        self.apartment = apartment
        self.renter = renter

    def to_dict(self):
        return {
            'id': self.id,
            'is_confirmed': self.is_confirmed,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'apartment': self.apartment.to_dict(),
            'renter': self.renter.to_dict()
        }

class ReviewsDTO:
    def __init__(self, review_id, description, point, renter_id, apartment, reservation_order):
        self.review_id = review_id
        self.description = description
        self.point = point
        self.renter = renter_id
        self.apartment = apartment
        self.reservation_order = reservation_order

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'description': self.description,
            'point': self.point,
            'renter': self.renter.to_dict(),
            'apartment': self.apartment.to_dict(),
            'reservation_order': self.reservation_order.to_dict()
        }



class TransactionDTO:
    def __init__(self, id, transaction_type, amount, reservation_order, apartment, renter):
        self.id = id
        self.transaction_type = transaction_type
        self.amount = amount
        self.reservation_order = reservation_order
        self.apartment = apartment
        self.renter = renter

    def to_dict(self):
        return {
            'id': self.id,
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'reservation_order': self.reservation_order.to_dict(),
            'apartment': self.apartment.to_dict(),
            'renter': self.renter.to_dict()
        }


class ApartmentRatingDTO:
    def __init__(self, rating_id, count_of_reviews, avg_point, time_created, time_modified):
        self.rating_id = rating_id
        self.count_of_reviews = count_of_reviews
        self.avg_point = avg_point
        self.time_created = time_created
        self.time_modified = time_modified

    def to_dict(self):
        return {
            'rating_id': self.rating_id,
            'count_of_reviews': self.count_of_reviews,
            'avg_point': self.avg_point,
            'time_created': self.time_created,
            'time_modified': self.time_modified
        }
