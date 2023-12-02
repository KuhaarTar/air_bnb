from app.dao.transation_dao import TransactionDAO
from app.dto import TransactionDTO


class TransactionService:
    @staticmethod
    def create_transaction(transaction_type, amount, reservation_order, apartment, renter):
        transaction = TransactionDAO.create_transaction(transaction_type, amount, reservation_order, apartment, renter)
        return TransactionDTO(transaction.id, transaction.transaction_type, transaction.amount,
                              transaction.reservation_order, transaction.apartment, transaction.renter)

    @staticmethod
    def get_transactions():
        transactions = TransactionDAO.get_transactions()
        return [TransactionDTO(transaction.id, transaction.transaction_type, transaction.amount,
                               transaction.reservation_order, transaction.apartment, transaction.renter)
                for transaction in transactions]

    @staticmethod
    def get_transaction_by_id(transaction_id):
        transaction = TransactionDAO.get_transaction_by_id(transaction_id)
        if transaction:
            return TransactionDTO(transaction.id, transaction.transaction_type, transaction.amount,
                                  transaction.reservation_order, transaction.apartment, transaction.renter)
        else:
            return None

    @staticmethod
    def update_transaction(transaction_id, transaction_type=None, amount=None, reservation_order=None,
                           apartment=None, renter=None):
        updated_transaction = TransactionDAO.update_transaction(transaction_id, transaction_type, amount,
                                                                reservation_order, apartment, renter)
        if updated_transaction:
            return TransactionDTO(updated_transaction.id, updated_transaction.transaction_type,
                                  updated_transaction.amount, updated_transaction.reservation_order,
                                  updated_transaction.apartment, updated_transaction.renter)
        else:
            return None

    @staticmethod
    def delete_transaction(transaction_id):
        deleted_transaction = TransactionDAO.delete_transaction(transaction_id)
        if deleted_transaction:
            return TransactionDTO(deleted_transaction.id, deleted_transaction.transaction_type,
                                  deleted_transaction.amount, deleted_transaction.reservation_order,
                                  deleted_transaction.apartment, deleted_transaction.renter)
        else:
            return None
