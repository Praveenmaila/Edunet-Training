from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f"{self.name}" 