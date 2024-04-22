from django.db import models


# Create your models here.
class Account(models.Model):
    owner_id = models.ForeignKey("customers.Customer", on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    last_transaction = models.DateTimeField()


class AccountBalanceHistory(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
