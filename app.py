from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store_monitoring.db'  # or your database URI
db = SQLAlchemy(app)

# Import your models after creating the app and db instances
from models import Store, BusinessHour, Timezone

# Code to populate data from CSV files
with app.app_context():
    with open('data/stores.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            store = Store(store_id=row['store_id'], timestamp_utc=row['timestamp_utc'], status=row['status'])
            db.session.add(store)
    db.session.commit()

    with open('data/business_hours.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            business_hour = BusinessHour(store_id=row['store_id'], day_of_week=row['day_of_week'],
                                         start_time_local=row['start_time_local'], end_time_local=row['end_time_local'])
            db.session.add(business_hour)
    db.session.commit()

    with open('data/timezones.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            timezone = Timezone(store_id=row['store_id'], timezone_str=row['timezone_str'])
            db.session.add(timezone)
    db.session.commit()

    # Route to list all stores
@app.route('/')
def list_stores():
    stores = Store.query.all()
    return render_template('list_stores.html', stores=stores)

# Route to show details of a specific store
@app.route('/store/<int:store_id>')
def show_store(store_id):
    store = Store.query.get(store_id)
    return render_template('show_store.html', store=store)

if __name__ == '__main__':
    app.run(debug=True)

# Rest of your code follows here

##
