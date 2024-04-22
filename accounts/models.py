import uuid

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Account(models.Model):
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner_id = models.ForeignKey("customers.Customer", on_delete=models.PROTECT)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    last_transaction = models.DateTimeField()

    class Meta:
        indexes = [
            models.Index("owner_id", name="Index accounts by owner id"),
        ]

    def __str__(self):
        short_id = self.account_id[:4] + "..." + self.account_id[-4:]
        return f"Account ID: {short_id}, owner_id: {self.owner_id}, last_updated: {self.date_modified}"


class HistoricAccountBalance(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    for_date = models.DateTimeField()

    class Meta:
        indexes = [
            models.Index(
                fields=["account_id", "for_date"], name="Index of account balances"
            )
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["account_id", "for_date"],
                name="Unique account balance for date",
            )
        ]

    def __str__(self):
        return f"Account {self.account_id} balance for date {self.for_date}"
