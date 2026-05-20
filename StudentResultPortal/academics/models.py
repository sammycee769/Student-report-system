from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from account.models import Student
from core.constants import LEVEL_CHOICES, SEMESTER_CHOICES
from core.models import Department


# Create your models here.

class AcademicSession(models.Model):
    name = models.CharField(max_length=20, help_text="e.g, 2024/2025")
    year = models.PositiveIntegerField(validators=[MinValueValidator(2000),MaxValueValidator(2100)])
    semester = models.CharField(max_length=10,choices=SEMESTER_CHOICES, default="first")
    is_current =models.BooleanField(default=False)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_semester_display()}"

    class Meta:
        db_table = 'academics_session'
        unique_together = [('year','semester')]
        ordering = ['-year','semester']

class Course(models.Model):
    department = models.ForeignKey(Department,on_delete=models.PROTECT,related_name='courses')
    course_code = models.CharField(max_length=20,unique=True)
    title = models.CharField(max_length=200)
    credit_units = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)])
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES,default="100")
    semester = models.CharField(max_length=10,choices=SEMESTER_CHOICES,default="first")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'academics_course'
        ordering = ['course_code']

    def __str__(self):
        return f"{self.course_code}: {self.title} ({self.credit_units} units)"

class CourseRegistration(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='registrations')
    course = models.ForeignKey(Course,on_delete=models.PROTECT,related_name='registrations')
    session = models.ForeignKey(AcademicSession,on_delete=models.PROTECT,related_name='registrations')
    register_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'academics_course_registration'
        unique_together = [('student','course','session')]
        ordering = ['-session__year','course__course_code']

    def __str__(self):
        return f"{self.student} - {self.course.course_code} ({self.session})"

    def clean(self):
        if self.course_id and self.session_id:
            if self.course.semester != self.session.semester:
                raise ValidationError(
                    f"Course '{self.course.course_code}' belongs to the"
                    f"{self.course.get_semester_display()} but this session"
                    f"is to {self.session.get_semester_display()}"
                )