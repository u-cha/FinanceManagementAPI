from django.contrib import admin
from .models import Customer

# Register your models here.


@admin.register(Customer)
class CustomerAdminModel(admin.ModelAdmin):
    list_filter = (
        "last_name",
        "birth_date",
    )
    search_fields = (
        "last_name",
        "birth_date",
    )
    ordering = (
        "last_name",
        "first_name",
    )
