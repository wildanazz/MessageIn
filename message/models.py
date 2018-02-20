from django.db import models

# Create your models here.

class Send(models.Model):
    sender = models.CharField(max_length=25)
    receiver = models.CharField(max_length=25)
    text = models.TextField()

