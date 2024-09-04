from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, unique=True, nullable=False)
    timestamp_utc = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(10), nullable=False)

class BusinessHour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    day_of_week = db.Column(db.Integer, nullable=False)
    start_time_local = db.Column(db.Time, nullable=False)
    end_time_local = db.Column(db.Time, nullable=False)

class Timezone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    timezone_str = db.Column(db.String(50), nullable=False)
