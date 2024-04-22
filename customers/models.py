from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    first_name = models.CharField()
    last_name = models.CharField()
    gender = models.CharField(choices=[("M", "Male"), ("F", "Female")])
    birth_date = models.DateField()
    address = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name", "birth_date"], name="Unique_customer"
            )
        ]

    def __str__(self):
        return f"Customer({self.first_name} {self.last_name})"
