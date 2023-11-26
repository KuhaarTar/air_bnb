from app import db
from app.models import Transaction


class TransactionDAO:
    @staticmethod
    def create_transaction(transaction_type, amount, reservation_order, apartment, renter):
        transaction = Transaction(
            transaction_type=transaction_type,
            amount=amount,
            reservation_order=reservation_order,
            apartment=apartment,
            renter=renter
        )
        db.session.add(transaction)
        db.session.commit()
        return transaction

    @staticmethod
    def get_transactions():
        return Transaction.query.all()

    @staticmethod
    def get_transaction_by_id(transaction_id):
        return Transaction.query.get(transaction_id)

    @staticmethod
    def update_transaction(transaction_id, transaction_type=None, amount=None, reservation_order=None,
                           apartment=None, renter=None):
        transaction = TransactionDAO.get_transaction_by_id(transaction_id)

        if transaction:
            if transaction_type:
                transaction.transaction_type = transaction_type
            if amount is not None:
                transaction.amount = amount
            if reservation_order:
                transaction.reservation_order = reservation_order
            if apartment:
                transaction.apartment = apartment
            if renter:
                transaction.renter = renter

            db.session.commit()

        return transaction

    @staticmethod
    def delete_transaction(transaction_id):
        transaction = TransactionDAO.get_transaction_by_id(transaction_id)

        if transaction:
            db.session.delete(transaction)
            db.session.commit()

        return transaction
