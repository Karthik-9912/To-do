from django.db import models

# Create your models here.
class RegistrationForm(models.Model):
    username=models.CharField(max_length=32)
    