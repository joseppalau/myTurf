from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Distributor(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name='products')
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Fertiliser(Product):
    nitrogen = models.DecimalField(max_digits=10, decimal_places=3)
    phosphorus = models.DecimalField(max_digits=10, decimal_places=3)
    potassium = models.DecimalField(max_digits=10, decimal_places=3)
    magnesium = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name


