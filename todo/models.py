# python3 manage.py runserver
# python3 manage.py makemigrations --dry-run
# python3 manage.py showmigrations
# python3 manage.py makemigrations --dry-plan
# python3 manage.py migrate --dry-plan
# python3 manage.py createsuperuser
# username: ckz8780, pantera101
from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
