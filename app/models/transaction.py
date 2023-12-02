from app import db


class Transaction(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    transaction_type = db.Column(db.String(150), nullable=False)
    amount = db.Column(db.DECIMAL, nullable=False)
    reservation_order_id = db.Column(db.BIGINT, db.ForeignKey('reservation_order.id'), nullable=False)
    apartment_id = db.Column(db.BIGINT, db.ForeignKey('reservation_order.apartment_id'), nullable=False)
    renter_id = db.Column(db.BIGINT, db.ForeignKey('reservation_order.renter_id'), nullable=False)
