from app import db
from app.models import Lessor


class LessorDAO:
    @staticmethod
    def create_lessor(email, phone, first_name, last_name):
        lessor = Lessor(email=email, phone=phone, first_name=first_name, last_name=last_name)
        db.session.add(lessor)
        db.session.commit()
        return lessor

    @staticmethod
    def get_lessors():
        return Lessor.query.all()

    @staticmethod
    def get_lessor_by_id(lessor_id):
        return Lessor.query.get(lessor_id)

    @staticmethod
    def update_lessor(lessor_id, email=None, phone=None, first_name=None, last_name=None):
        lessor = LessorDAO.get_lessor_by_id(lessor_id)

        if lessor:
            if email:
                lessor.email = email
            if phone:
                lessor.phone = phone
            if first_name:
                lessor.first_name = first_name
            if last_name:
                lessor.last_name = last_name

            db.session.commit()

        return lessor

    @staticmethod
    def delete_lessor(lessor_id):
        lessor = LessorDAO.get_lessor_by_id(lessor_id)

        if lessor:
            db.session.delete(lessor)
            db.session.commit()

        return lessor
