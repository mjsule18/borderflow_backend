from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_business = models.BooleanField(default=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100)
    

# Create your models here.
