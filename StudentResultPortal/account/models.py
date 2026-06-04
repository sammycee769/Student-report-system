from django.db import models

from account.util import generate_matric_number
from core.constants import LEVEL_CHOICES, ROLE_STUDENT
from core.models import User, Department

# Create your models here.
class Student(models.Model):

    STUDENT_STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("suspended", "Suspended"),
        ("withdrawn","Withdrawn"),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="100")
    status = models.CharField(max_length=20, choices=STUDENT_STATUS_CHOICES, default="active")
    matric_number = models.CharField(max_length=20, unique=True, default=generate_matric_number,primary_key=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='student_profile',limit_choices_to={"role": ROLE_STUDENT})
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entry_year = models.PositiveIntegerField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.matric_number

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email

    @property
    def is_active(self):
        return self.status

class Staff(models.Model):
    DESIGNATION_CHOICES = [
        ("L1","Lecturer I"),
        ("L2", "Lecturer II"),
        ("SLR","Senior Lecturer"),
        ("PRF","Professor"),
        ("HOD","Head Of Department")
    ]
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    designation = models.CharField(max_length=55, null=False, blank=False,choices=DESIGNATION_CHOICES,default="L1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.designation}"

    class Meta:
        ordering = ['designation']