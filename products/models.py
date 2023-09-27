from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/images/")
    description = models.TextField()
    price = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'