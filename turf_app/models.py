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
    type = models.CharField(max_length=100, default='Fertilizer')  # whether it is to be used in a solid or liquid application
    units = models.CharField(default='l', max_length=20, blank=True)

    def __str__(self):
        return self.name


class Fertiliser(Product):
    N = models.DecimalField(max_digits=10, decimal_places=3)
    P = models.DecimalField(max_digits=10, decimal_places=3)
    K = models.DecimalField(max_digits=10, decimal_places=3)
    Mg = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.DecimalField(default=0.0, max_digits=10, decimal_places=3) # amount of use by users

    def __str__(self):
        return self.name


class FertiliserUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fertilisers', blank=True)
    distributor = models.ForeignKey(DistributorUser, on_delete=models.CASCADE, related_name='fertilisers', null=True, blank=True)
    fertiliser = models.ForeignKey(Fertiliser, on_delete=models.PROTECT, related_name='used_by', blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=3, default=0) #amount used with all applications
    stock = models.DecimalField(default=0.0, max_digits=10, decimal_places=3) #amount at warehouse
    price = models.DecimalField(default=1.0, max_digits=10, decimal_places=3)


class FertiliserInUse(models.Model):
    fertiliser = models.ForeignKey(FertiliserUser, null=True, on_delete=models.SET_NULL, related_name='actions')
    quantity = models.DecimalField(max_digits=10, decimal_places=3)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='applications')
    type = models.CharField(max_length=50)
    units = models.CharField(max_length=20, default='l')
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    products = models.ManyToManyField(FertiliserInUse, related_name='applications')
    scheduled_date = models.DateTimeField(default=timezone.now)
    done_date = models.DateTimeField(null=True, blank=True)

    def application_finished(self):
        self.done_date = timezone.now()
        self.save()







