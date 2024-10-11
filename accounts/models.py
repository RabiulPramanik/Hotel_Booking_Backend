from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserModel(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="accounts/profile_images/")
    balance = models.FloatField(default=0.00, null=True, blank=True)

    def __str__(self):
        return self.user.username
