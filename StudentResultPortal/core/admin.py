from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import Department, User


# Register your models here.
# admin.site.register(Department)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','description','code','created_at')
    list_per_page = 10

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('username','email','is_staff','is_active','last_login')
