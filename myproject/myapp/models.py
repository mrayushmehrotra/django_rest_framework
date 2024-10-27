# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Specify a unique related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Specify a unique related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

class SpamReport(models.Model):
    phone_number = models.CharField(max_length=15)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spam_reports')
    created_at = models.DateTimeField(auto_now_add=True)
