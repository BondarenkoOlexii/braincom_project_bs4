"""
Create main models for braincom_project
"""


from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=225)
    color = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=225)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    promotion_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    photos = ArrayField(models.CharField(null=True, blank=True))
    code = models.CharField(max_length=100)
    numb_of_reviews = models.CharField(null=True, blank=True)
    display_resolution = models.CharField(max_length=100)
    product_specification = models.JSONField(default=dict)

    def __str__(self):
        return self.name
