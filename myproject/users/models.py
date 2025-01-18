from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(min_length=5, max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.name
# Create your models here.
