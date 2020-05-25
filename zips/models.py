from django.db import models

# Create your models here.
class Zip(models.Model):
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
