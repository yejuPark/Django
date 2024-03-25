from django.db import models

# Create your models here.

class Actor(models.Model):
  name = models.CharField(max_length=100)


class Movie(models.Model):
  title = models.CharField(max_length=100)
  actors = models.ManyToManyField(Actor, related_name='movies')