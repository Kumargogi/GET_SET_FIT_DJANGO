from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

