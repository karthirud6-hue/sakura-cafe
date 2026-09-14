from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    availability = models.BooleanField(default=True)
    picture = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/'
    )

    def __str__(self):
        return self.product_name