from django.db import models

# Create your models here.
class Car(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    mileage = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255)
    modified_date = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title