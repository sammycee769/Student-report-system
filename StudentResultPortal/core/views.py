import code
from loguru import logger

from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from core.models import Department
from core.serializers import DepartmentSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
# @api_view(['POST'])
# def create_department(request):
#     try:
#         serializer = DepartmentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         name = serializer.validated_data['name']
#         logger.info(f"data validated for department {name}")
#
#         if Department.objects.filter(code=serializer.validated_data['code']).exists():
#             logger.info(f"Department with code {serializer.validated_data['code']} already exists")
#             return Response({"message": "department already exists"},status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         logger.info(f"department {name} created")
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         logger.error(f"Error creating department {str(e)}")
#         return Response({"message": "department with this detail already exists"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# @api_view(['GET'])
# def get_department(request,code):
#     try:
#         department = Department.objects.get(code=code)
#         serializer = DepartmentSerializer(department)
#         logger.info(f"data retrieved for department {department.name} with code {code}")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Department.DoesNotExist:
#         logger.error(f"Department with code {code} does not exist")
#         return Response({'message': f'department with this code {code} does not exist'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         logger.error(f"Error retrieving department {str(e)}")
#         return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# @api_view(['PUT','PATCH'])
# def update_department(request,code):
#     try:
#         department = Department.objects.get(code=code)
#         is_partial_update = request.method == 'PATCH'
#         serializer = DepartmentSerializer(department,data=request.data, partial=is_partial_update)
#         serializer.is_valid(raise_exception=True)
#
#         new_code = serializer.validated_data['code']
#         if new_code and new_code != department.code:
#             if Department.objects.filter(code=new_code).exists():
#                 logger.error(f"Department with code {new_code} already exists")
#                 return Response({"message": "Department with this code already exists"}, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         logger.info(f"department {new_code} updated")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Department.DoesNotExist:
#         logger.error(f"Department with code {code} does not exist")
#         return Response({"message": "Department with this code does not exist"}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         logger.error(f"Error updating department {str(e)}")
#         return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return [IsAdminUser()]
        return [AllowAny()]