from datetime import datetime
from  app import db, Store

# Sample data
stores_data = [
    {'store_id': 8419537941919820732, 'timestamp_utc': datetime(2023, 1, 22, 12, 9, 39, 388884), 'status': 'active'},
    # ... other data ...
]

# Insert data
for store_data in stores_data:
    new_store = Store(
        store_id=store_data['store_id'],
        timestamp_utc=store_data['timestamp_utc'],
        status=store_data['status']
    )
    db.session.add(new_store)

db.session.commit()
