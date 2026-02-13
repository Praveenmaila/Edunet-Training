from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    ratings= models.FloatField()
    image_url = models.CharField(max_length=200)
    reviews = models.FloatField()


    def __str__(self):
        return self.title