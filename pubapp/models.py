from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Venue(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    date = models.DateField()


class Publication(models.Model):
    title = models.CharField(max_length=120)
    author = models.ManyToManyField(Author)
    date = models.IntegerField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
