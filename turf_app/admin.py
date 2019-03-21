from django.contrib import admin
from .models import Manufacturer, Distributor, Field, Fertiliser, Application
# Register your models here.


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Manufacturer


class DistributorAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Distributor


class FieldAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'width', 'length']

    class Meta:
        model = Field


class FertiliserAdmin(admin.ModelAdmin):
    list_display = ['N', 'P', 'K']

    class Meta:
        model = Fertiliser


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'field', 'scheduled_date']

    class Meta:
        model = Application


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Fertiliser, FertiliserAdmin)
admin.site.register(Application, ApplicationAdmin)