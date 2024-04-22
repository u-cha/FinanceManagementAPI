from django.contrib import admin
from .models import Transaction

# Register your models here.


@admin.register(Transaction)
class TransactionAdminModel(admin.ModelAdmin):
    list_filter = (
        "customer_id",
        "type",
        "currency_id",
        "account_id",
        "created_at",
        "amount",
    )
    search_fields = (
        "customer_id",
        "type",
        "currency_id",
        "account_id",
        "created_at",
        "amount",
    )
    ordering = (
        "customer_id",
        "-created_at",
    )
