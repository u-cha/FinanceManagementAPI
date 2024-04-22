from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField()
    last_name = models.CharField()
    gender = models.CharField(choices=[("M", "Male"), ("F", "Female")])
    birth_date = models.DateField()
    address = models.TextField()
