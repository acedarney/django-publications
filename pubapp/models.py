from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Venue(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return '{}'.format(self.name)


class Publication(models.Model):
    title = models.CharField(max_length=120)
    author = models.ManyToManyField(Author)
    date = models.IntegerField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):

        return '{}'.format(self.title)
