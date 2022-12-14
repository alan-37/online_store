from django.db import models
from PIL import Image


class Product(models.Model):
    T_SHIRT = 't-shirt'
    BLOUSE = 'blouse'
    HEADDRESS = 'headdress'
    PATCH = 'patch'
    BAG = 'bag'

    CHOICE_GROUP = {
        (T_SHIRT, 't-shirt'),
        (BLOUSE, 'blouse'),
        (HEADDRESS, 'headdress'),
        (PATCH, 'patch'),
        (BAG, 'bag'),

    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    availability = models.BooleanField(default=True)
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=T_SHIRT)
    images = models.ImageField(default="no_image.png", upload_to='product_image')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.name}'
