from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from core.constants import ROLE_CHOICES, ROLE_ADMIN


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(max_length=250, unique=True, blank=False, null=False)
    username = models.CharField(max_length=250, unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="student")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REDIRECT_FIELD = ['username']

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


    @property
    def is_admin(self):
        return self.role == ROLE_ADMIN




class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.code} - {self.name}"