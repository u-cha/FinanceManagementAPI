from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Currency(models.Model):
    code = models.CharField(
        "Currency code", max_length=3, unique=True, validators=[MinLengthValidator(3)]
    )
    name = models.CharField("Currency name", max_length=50)
    symbol = models.CharField("Currency symbol", null=True, blank=True, unique=True)
