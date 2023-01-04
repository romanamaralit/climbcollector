from django.db import models

# Create your models here.
class Climb(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location =  models.TextField(max_length=250)
    people = models.IntegerField()


    def __str__(self):
        return f'{self.name} ({self.id})'