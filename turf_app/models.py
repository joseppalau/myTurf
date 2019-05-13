from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Field(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=100)
    width = models.DecimalField(max_digits=10, decimal_places=3)
    length = models.DecimalField(max_digits=10, decimal_places=3)
    units = models.CharField(default='m', max_length=20)
    units_dimension = models.CharField(default='m2', max_length=20)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    #city_weather_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def calc_dim(self):
        return self.width * self.length


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Distributor(models.Model):
    manufacturers = models.ManyToManyField(Manufacturer, related_name='distributors')
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank = True)

    def __str__(self):
        return self.name


class DistributorUser(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name='clients')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='distributors')


class Product(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    package = models.CharField(max_length=100, null=True, blank=True)
    quantity_per_package = models.DecimalField(default=0.0, max_digits=10, decimal_places=3, null=True, blank=True)
    units = models.CharField(default='L', max_length=20)

    def __str__(self):
        return self.name


class Fertiliser(Product):
    N = models.DecimalField(max_digits=10, decimal_places=3)
    P = models.DecimalField(max_digits=10, decimal_places=3)
    K = models.DecimalField(max_digits=10, decimal_places=3)
    Mg = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(default='Liquid', max_length=50)
    quantity = models.DecimalField(default=0.0, max_digits=10, decimal_places=3) # amount of use by users

    def __str__(self):
        return self.name


class FertiliserUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fertilisers', blank=True)
    distributor = models.ForeignKey(DistributorUser, on_delete=models.CASCADE, related_name='fertilisers', null=True, blank=True)
    fertiliser = models.ForeignKey(Fertiliser, on_delete=models.PROTECT, related_name='used_by', blank=True)
    stock = models.DecimalField(default=0.0, max_digits=10, decimal_places=3) #amount at warehouse
    price = models.DecimalField(default=1.0, max_digits=10, decimal_places=3)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='applications')
    type = models.CharField(max_length=50)
    units = models.CharField(max_length=20, default='l')
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    scheduled_date = models.DateTimeField(default=timezone.now)
    done_date = models.DateTimeField(null=True, blank=True)

    def application_finished(self):
        for i in range(len(self.products_used)):
            self.products_used[i].fertiliser.stock -= self.products_used[i].quantity
        self.save()


class FertiliserInUse(models.Model):
    fertiliser = models.ForeignKey(FertiliserUser, null=True, on_delete=models.SET_NULL, related_name='replies')
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    application = models.ForeignKey(Application, null=True, on_delete=models.CASCADE, related_name='products_used')









