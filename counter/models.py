from django.db import models

# Create your models here.

class History(models.Model):
    text = models.CharField(max_length=10000)
    num_of_text = models.IntegerField()
