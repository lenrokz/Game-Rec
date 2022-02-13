from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    pass

class Comment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="usercomment")
     content = models.CharField(max_length=100)

class Game (models.Model):
    image = models.URLField(max_length=200)
    title = models.CharField(max_length=64)
    description1 = models.CharField(max_length=500)
    description2 = models.CharField(max_length=500)
    description3 = models.CharField(max_length=500)
    description4 = models.CharField(max_length=500)
    description5 = models.CharField(max_length=500, default="Release date:")
    date = models.CharField(max_length=64)
    genre = models.CharField(max_length=64, default="Action")
    system = models.CharField(max_length=64, default="Multiplatform")
    xbox = models.URLField(max_length=200)
    pc = models.URLField(max_length=200)
    playstation = models.URLField(max_length=200)
    comment = models.ManyToManyField(Comment, blank=True, related_name="comments")

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.URLField(max_length=200)
    description = models.CharField(max_length=64, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="images")    
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="watchuser")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="watchedgame") 
    
class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    liked_game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="liked_game")