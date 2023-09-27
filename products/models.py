from django.db import models

from apps.common.models import BaseModel


class Product(BaseModel, models.Model):
    class Type(models.TextChoices):
        TRINAJOR = 'trinajor'
        YEGULIK = 'yegulik'
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/images/")
    description = models.TextField()
    price = models.IntegerField()
    amount = models.IntegerField()
    type_choice = models.CharField(max_length=10, choices=Type.choices)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'