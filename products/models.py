from django.db import models


class Product(models.Model):

    product_categories = [
        ('Vegetables', 'Vegetables'),
        ('Friuts', 'Friuts'),
        ('Candies', 'Candies'),
        ('Beverages', 'Beverages'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=product_categories)
    price = models.PositiveIntegerField()
    sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
