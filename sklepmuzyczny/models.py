from django.db import models
from django.utils import timezone

class Cart(models.Model):
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return "Koszyk uzytkownika:" + author 
        
class Disc(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    available_count = models.IntegerField()

    carts = models.ManyToManyField(Cart)

    
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.title
