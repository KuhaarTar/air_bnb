from app import db
from app.models import Renter


class RenterDAO:
    @staticmethod
    def create_renter(first_name, last_name, email, phone):
        renter = Renter(first_name=first_name, last_name=last_name, email=email, phone=phone)
        db.session.add(renter)
        db.session.commit()
        return renter

    @staticmethod
    def get_renters():
        return Renter.query.all()

    @staticmethod
    def get_renter_by_id(renter_id):
        return Renter.query.get(renter_id)

    @staticmethod
    def update_renter(renter_id, first_name=None, last_name=None, email=None, phone=None):
        renter = RenterDAO.get_renter_by_id(renter_id)

        if renter:
            if first_name:
                renter.first_name = first_name
            if last_name:
                renter.last_name = last_name
            if email:
                renter.email = email
            if phone:
                renter.phone = phone

            db.session.commit()

        return renter

    @staticmethod
    def delete_renter(renter_id):
        renter = RenterDAO.get_renter_by_id(renter_id)

        if renter:
            db.session.delete(renter)
            db.session.commit()

        return renter
