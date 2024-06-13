from django.db import models

# Create your models here.
class MonSysteme(models.Model):
    titre = models.CharField(max_length=100)
    etat = models.IntegerField(default=0)
    
class Zone(models.Model):
    titre = models.CharField(max_length=100)
    etat = models.IntegerField(default=0)