from django.db import models

# PS C:\-- Phyton\-- Django\02 back up - kopie\Django-poj_app-main> py manage.py makemigrations
# Migrations for 'app_pojistovna':
#   app_pojistovna\migrations\0001_initial.py
#     - Create model Record

# py manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, app_pojistovna, auth, contenttypes, sessions
# Running migrations:
#   Applying app_pojistovna.0001_initial... OK



class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")


