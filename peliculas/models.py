from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=200)
    actor = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, related_name="characters", on_delete=models.CASCADE)    

    def __str__(self):
        return self.name
