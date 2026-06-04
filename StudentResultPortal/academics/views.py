from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from academics.models import Course, AcademicSession
from academics.serializers import CourseSerialiser, AcademicSessionSerialiser, ReadAcademicSessionSerialiser


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerialiser

    def get_queryset(self):
        return Course.objects.filter(department=self.kwargs['nested_1_pk'])

    def get_serializer_context(self):
        return {"department_id": self.kwargs.get("nested_1_pk")}

class AcademicSessionViewSet(viewsets.ModelViewSet):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerialiser

class AcademicSessionView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = AcademicSessionSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request,*args,**kwargs):
        academic_sessions = AcademicSession.objects.all()
        ReadAcademicSessionSerialiser(academic_sessions,many=True)

class GetUpdateDeleteAcademicSessionView(RetrieveUpdateDestroyAPIView):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerialiser