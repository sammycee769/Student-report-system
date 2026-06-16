from django.urls import path, include
from . import views
from rest_framework.views import APIView

from academics.views import AcademicSessionViewSet,AcademicSessionView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course-registration', views.CourseRegistrationViewSet, basename='course-registration')

urlpatterns = [
    path('',include(router.urls)),
    path('session/',views.AcademicSessionView.as_view(),name='session'),
    path('session/<int:pk>/', views.GetUpdateDeleteAcademicSessionView.as_view(), name='session-detail'),
]