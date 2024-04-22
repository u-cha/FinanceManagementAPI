from django.contrib import admin
from .models import Account, HistoricAccountBalance

# Register your models here.


@admin.register(Account)
class AccountAdminModel(admin.ModelAdmin):
    list_filter = (
        "owner_id",
        "date_created",
        "date_modified",
    )
    search_fields = (
        "account_id",
        "owner_id",
    )
    ordering = ("-date_created",)


@admin.register(HistoricAccountBalance)
class HistoricAccountBalanceAdminModel(admin.ModelAdmin):
    list_filter = (
        "account_id",
        "for_date",
    )
    ordering = (
        "account_id",
        "-for_date",
    )
