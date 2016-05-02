from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from decimal import Decimal

@python_2_unicode_compatible
class Provider(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(null=True, unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    language = models.CharField(max_length=30, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class PolygonArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    provider = models.ForeignKey(Provider)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    pricing = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

