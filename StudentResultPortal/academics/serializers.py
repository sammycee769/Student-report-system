from rest_framework import serializers

from academics.models import Course, AcademicSession


class CourseSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_code','title','level','semester','description','credit_units']

    def create(self, validated_data):
        department_id = self.context.get("department_id")
        return Course.objects.create(department_id=department_id, **validated_data)

class AcademicSessionSerialiser(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = ['name','year','semester','is_current','start_date','end-date']

class ReadAcademicSessionSerialiser(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = ['name','year','start_date','is_current']