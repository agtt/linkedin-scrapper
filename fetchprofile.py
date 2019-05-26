from db import db

db = db()

profiles = db.query('SELECT * FROM `scrappers` ORDER BY `id` DESC limit 5')
for profile in profiles:
    link = "https://www.linkedin.com/in/" + profile[1]
    print(link)
