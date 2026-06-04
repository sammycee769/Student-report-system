from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from core.constants import ROLE_CHOICES, ROLE_ADMIN


class UserManager(BaseUserManager):

    def get_by_natural_key(self, email):
        return self.get(email=email)


    def create_user(self, email,username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", ROLE_ADMIN)
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    objects = UserManager()
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(max_length=250, unique=True, blank=False, null=False)
    username = models.CharField(max_length=250, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="student")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

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
    name = models.CharField(max_length=200, unique=True,blank=False, null=False)
    code = models.CharField(max_length=20, unique=True,primary_key=True,blank=False, null=False)
    description = models.TextField(blank=False,null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_department"
        ordering = ['name']



    def __str__(self):
        return f"{self.code} - {self.name}"