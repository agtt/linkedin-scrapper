import sys
import json
import time
from LinkedinController import LinkedinController

from db import db

db = db()
linkedin = LinkedinController(config=True, debug=True)
linkedin.login()
profiles = db.query('SELECT * FROM `scrappers` ORDER BY `id` ASC limit 2')
for profile in profiles:
    link = "https://www.linkedin.com/in/" + profile[1]
    print(link)
    try:
        data = linkedin.profile(link)
        db.updateprofile(profile[0], data) #update safe data
        time.sleep(2)
        # Update Profile
    except Exception as e:
        print(str(e))
        print('Profile Error')
