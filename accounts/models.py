from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=255)
