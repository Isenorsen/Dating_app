from django.db import models
from django.contrib.auth.models import User


class UserAccounts(models.Model):
    user_account_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    about = models.TextField(max_length=2000, blank=True)
    avatar = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.name
