from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Define choices for gender
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    
    # Add the gender field
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
