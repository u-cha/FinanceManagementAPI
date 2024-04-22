import uuid

from django.db import models


# Create your models here.
class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        REFILL = "REFILL"
        SPENDING = "SPENDING"

    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer_id = models.ForeignKey("customers.Customer", on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    type = models.TextField(
        choices=TransactionType.choices, default=TransactionType.SPENDING
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency_id = models.ForeignKey("currencies.Currency", on_delete=models.PROTECT)
    account_id = models.ForeignKey("accounts.Account", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["customer_id"], name="customer_id_index"),
            models.Index(fields=["account_id"], name="account_id_index"),
        ]
