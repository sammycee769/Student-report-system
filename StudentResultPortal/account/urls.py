from django.urls import path
from account import views
from rest_framework.views import APIView

urlpatterns = [
    path('student-enroll',views.StudentEnrollment.as_view(),name='student-enroll'),
    path('staff-enroll',views.StaffEnrollment.as_view(),name='staff-enroll'),
    path("auth/login/",views.LoginView.as_view(),name="login"),
]