from logging import raiseExceptions

from django.db import transaction
from django.db.models import Model
from django.shortcuts import render
from loguru import logger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Student, Staff
from core.models import User, Department
from account.serializers import StudentEnrollmentSerializers, StaffRegistrationSerializers


# Create your views here.
class StudentEnrollment(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = StudentEnrollmentSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)

            code = serializer.validated_data['department']
            department = Department.objects.get(code=code)
            if not Department.objects.filter(code=code).exists():
                return Response({"message": "Department does not exist"}, status=status.HTTP_404_NOT_FOUND)

            with transaction.atomic():
                user=User.objects.create(
                    email = serializer.validated_data['email'],
                    username = serializer.validated_data['username'],
                    first_name = serializer.validated_data['first_name'],
                    last_name = serializer.validated_data['last_name'],
                    password = serializer.validated_data['password']
                )
                user.set_password(serializer.validated_data["password"])
                student = Student.objects.create(
                    user=user,
                    department = department,
                    entry_year = serializer.validated_data['entry_year'],
                )
                user.save()
                student.save()
                logger.info(f"Student has been created successfully")
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creaating student {str(e)}")
            return Response({"message": "Error enrolling Student"}, status=status.HTTP_400_BAD_REQUEST)

class StaffEnrollment(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = StaffRegistrationSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)

            code = serializer.validated_data['department']
            department = Department.objects.get(code=code)
            if not Department.objects.filter(code=code).exists():
                return Response({"message": "Department does not exist"}, status=status.HTTP_404_NOT_FOUND)
            with transaction.atomic():
                user=User.objects.create(
                    email = serializer.validated_data['email'],
                    username = serializer.validated_data['username'],
                    first_name = serializer.validated_data['first_name'],
                    last_name = serializer.validated_data['last_name'],
                    password = serializer.validated_data['password'],
                    role = "staff"

                )
                user.set_password(serializer.validated_data["password"])
                staff = Staff.objects.create(
                    user=user,
                    department = department,
                )
                user.save()
                staff.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
                logger.error(f"Error enrolling Staff {str(e)}")
                return Response({"message": "Error  Staff"}, status=status.HTTP_400_BAD_REQUEST)

