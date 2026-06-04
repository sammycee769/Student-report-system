from django.urls import path, include
from . import views
from rest_framework.views import APIView

from academics.views import AcademicSessionViewSet,AcademicSessionView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',AcademicSessionViewSet,basename='academic-session')

urlpatterns = [
    path('',include(router.urls)),
    path('session/',views.AcademicSessionView.as_view(),name='session')
]