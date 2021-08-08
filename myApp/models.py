from django.db import models
from django.contrib.auth.models import User


CHOICES = (
        ('Following', 'Following'),
        ('Done', 'Done'),
        ('Wish', 'Wish'),
    )

# Create your models here.
class Anime(models.Model):
    user    =   models.ForeignKey(User, on_delete=models.CASCADE)
    title   =   models.CharField(max_length=200,null=False)
    status  =   models.CharField(max_length=200,choices = CHOICES,null=False)
    last    =   models.IntegerField(null=True)
    url_photo=  models.CharField(max_length=500)


    def __str__(self):
        return self.title