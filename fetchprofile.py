from db import db
db = db()

profiles = db.query('SELECT * FROM `scrappers` ORDER BY `id` DESC limit 5')
for profile in profiles:
    print(profile)