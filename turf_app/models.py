from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Field(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=100)
    width = models.DecimalField(max_digits=10, decimal_places=3)
    length = models.DecimalField(max_digits=10, decimal_places=3)
    units = models.CharField(null=True, max_length=20)
    units_dimension = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.name

    def calc_dim(self):
        return self.width * self.length


class Manufacturer(models.Model):
    user = models.ManyToManyField(User, related_name='manufacturers')
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Distributor(models.Model):
    user = models.ManyToManyField(User, related_name='distributors')
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name='products')
    type = models.CharField(max_length=100)  # whether it is to be used in a solid or liquid application
    units = models.CharField(null=True, max_length=20)
    stock = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name


class Fertiliser(Product):
    N = models.DecimalField(max_digits=10, decimal_places=3)
    P = models.DecimalField(max_digits=10, decimal_places=3)
    K = models.DecimalField(max_digits=10, decimal_places=3)
    Mg = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='applications')
    type = models.CharField(max_length=50)
    units = models.CharField(null=True, max_length=20)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    products = models.ManyToManyField(Product, related_name='applications')
    scheduled_date = models.DateTimeField(blank=True, null=True)
    done_date = models.DateTimeField(null=True)

    def application_finished(self):
        self.done_date = timezone.now()
        self.save()

