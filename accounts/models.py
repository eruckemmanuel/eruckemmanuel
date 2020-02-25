from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail_dir = models.CharField(max_length=1000, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/profile/', null=True)
    date_registered = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.first_name +' '+self.user.last_name



class PhoneVerificationCodes(models.Model):
    phone = models.CharField(max_length=20)
    code = models.CharField(max_length=8)
    date_sent = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    date_verified = models.DateTimeField(auto_now=False, null=True, blank=True)
    expired = models.BooleanField(default=False)
