from django.contrib import admin
from .models import Manufacturer, Distributor, Fertiliser
# Register your models here.

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']

