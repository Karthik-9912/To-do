from django.db import models

# Create your models here.
class To_Do(models.Model):
    task=models.CharField(max_length=100)
    desc=models.TextField()