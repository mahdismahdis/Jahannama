from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    # انگلیسی
    name_en = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )
    description_en = models.TextField(
        blank=True,
        default=""
    )

    # عربی
    name_ar = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )
    description_ar = models.TextField(
        blank=True,
        default=""
    )
    image = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # انگلیسی
    title_en = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )
    description_en = models.TextField(
        blank=True,
        default=""
    )

    # عربی
    title_ar = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )
    description_ar = models.TextField(
        blank=True,
        default=""
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10,db_index=True)
    image = models.CharField(max_length=200, default="")
    stock = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (100 - self.discount) / 100
        return self.price

    def __str__(self):
         return self.title


class Gallery(models.Model):
        image = models.ImageField(upload_to='gallery/')
        title = models.CharField(max_length=100, blank=True)

        def __str__(self):
            return self.title or f"Image {self.id}"