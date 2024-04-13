from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genres(models.Model):
    genres=models.CharField(max_length=342)

    def __str__(self):
        return self.genres
class Movies(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()
    release_date=models.DateField()
    actor=models.CharField(max_length=233)
    genres=models.ForeignKey(Genres,on_delete=models.CASCADE)
    youtube=models.URLField()
    added_user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Review(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    added_user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.TextField()
    rating=models.IntegerField()


    def __str__(self):
        return str(self.movie)