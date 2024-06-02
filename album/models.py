from django.db import models
from musician.models import Musician
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=60)
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    album_release_date = models.DateField()
    rating = models.IntegerField(default=1,
     validators=[MaxValueValidator(5),MinValueValidator(1)])

    def __str__(self):
        return self.album_name

