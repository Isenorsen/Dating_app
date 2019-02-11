from django.db import models
from accounts.models import UserAccounts
import datetime
from django.utils import timezone

class DatingForm(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(UserAccounts, on_delete=models.DO_NOTHING, blank=True, default=0)
    text = models.TextField()
    image1 = models.ImageField(upload_to='media', blank=True)
    image2 = models.ImageField(upload_to='media', blank=True)
    image3 = models.ImageField(upload_to='media', blank=True)
    date = models.DateField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.title