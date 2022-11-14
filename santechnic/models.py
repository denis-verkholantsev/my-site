from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200, default="", primary_key=True)
    category_image = models.ImageField(default="", upload_to='images/')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    product_name = models.CharField(max_length=200, primary_key=True)
    product_price = models.FloatField(default=0.0)
    product_image = models.ImageField(default="", upload_to='images/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

