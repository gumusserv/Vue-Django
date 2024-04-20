# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=150, unique=True, primary_key=True)
#     password = models.CharField(max_length=128)

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=150, unique=True, primary_key=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)


