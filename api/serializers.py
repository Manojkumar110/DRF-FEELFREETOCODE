from rest_framework import serializers
from api.models import Employee
from django .contrib.auth.models import User
from courseapi.models import Course

# step :- 1
# class EmployeeSerializer(serializers.serializer):
#     name = serializers.CharField(max_length=50)
#     email = serializers.EmailField(max_length=50)
#     password = serializers.CharField(max_length=20)
#     phone = serializers.IntegerField()

    # def create(self, validated_data):
    #     print('Create method Called..')
    #     return Employee.objects.create(**validated_data)

    # def update(self, Employee , validated_data):
    #     print('Update method Called..')
    #     newEmp = Employee(**validated_data)
    #     newEmp.id = Employee.id
    #     newEmp.save()
    #     return newEmp


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=30)
#     email = serializers.EmailField()
#     password = serializers.CharField()

# --------------------------------------------------------------------



# step:-2
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
   class Meta:
    model = User
    fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'