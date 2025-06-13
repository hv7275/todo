from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  bio = models.TextField(blank=True)
  phone_no = models.CharField(max_length=15)
  profile_pic = models.ImageField(upload_to='account/', blank=True, null=True)
  
  def __str__(self):
    return self.user
  
