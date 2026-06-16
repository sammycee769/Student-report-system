from django.contrib import admin

from account.models import Student,Staff


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user","matric_number","department","level","status")
    search_fields = ("user__email","matric_number")

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("user","department","designation")
    search_fields = (["user__email"])
