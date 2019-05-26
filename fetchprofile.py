import sys
import json
import time
from LinkedinController import LinkedinController

from db import db

db = db()
linkedin = LinkedinController(config=True, debug=True)
linkedin.login()
profiles = db.query('SELECT * FROM `scrappers` ORDER BY `id` DESC limit 5')
for profile in profiles:
    link = "https://www.linkedin.com/in/" + profile[1]
    print(link)
    try:
        data = linkedin.profile(link)
        print(data)
        time.sleep(2)
        # Update Profile
    except Exception as e:
        print('Profile Error')
