from django.urls import path, include

from rest_framework_nested import routers

from core.views import DepartmentViewSet
from academics.views import CourseViewSet

router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet, basename='departments')
dept_router = routers.NestedDefaultRouter(router, parent_prefix='departments')
dept_router.register('course', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
    path('',include(dept_router.urls)),
    # path(route='create_department/', view=create_department, name='create_department'),
    # path('get_department/<str:code>/', get_department, name='get_department'),
    # path('update_department/<str:code>/', update_department, name='update_department'),
]