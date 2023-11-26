from app.dao.lessor_dao import LessorDAO
from app.dto import LessorDTO


class LessorService:
    @staticmethod
    def create_lessor(email, phone, first_name, last_name):
        lessor = LessorDAO.create_lessor(email, phone, first_name, last_name)
        return LessorDTO(id=lessor.id, email=lessor.email, phone=lessor.phone, first_name=lessor.first_name,
                         last_name=lessor.last_name)

    @staticmethod
    def get_lessors():
        lessors = LessorDAO.get_lessors()
        return [LessorDTO(id=lessor.id, email=lessor.email, phone=lessor.phone, first_name=lessor.first_name,
                          last_name=lessor.last_name) for lessor in lessors]

    @staticmethod
    def get_lessor_by_id(lessor_id):
        lessor = LessorDAO.get_lessor_by_id(lessor_id)
        return LessorDTO(id=lessor.id, email=lessor.email, phone=lessor.phone, first_name=lessor.first_name,
                         last_name=lessor.last_name) if lessor else None

    @staticmethod
    def update_lessor(lessor_id, email=None, phone=None, first_name=None, last_name=None):
        updated_lessor = LessorDAO.update_lessor(lessor_id, email, phone, first_name, last_name)
        return LessorDTO(id=updated_lessor.id, email=updated_lessor.email, phone=updated_lessor.phone,
                         first_name=updated_lessor.first_name,
                         last_name=updated_lessor.last_name) if updated_lessor else None

    @staticmethod
    def delete_lessor(lessor_id):
        deleted_lessor = LessorDAO.delete_lessor(lessor_id)
        return LessorDTO(id=deleted_lessor.id, email=deleted_lessor.email, phone=deleted_lessor.phone,
                         first_name=deleted_lessor.first_name,
                         last_name=deleted_lessor.last_name) if deleted_lessor else None
