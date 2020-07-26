from django.db import models

# Create your models here.
class Kist(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=100)
    category = models.CharField(max_length=100)