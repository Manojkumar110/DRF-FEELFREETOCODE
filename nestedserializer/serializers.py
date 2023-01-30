from rest_framework import serializers
from nestedserializer.models import Courses, Instructor


# model Serializer start here :-

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Courses
#         fields = '__all__'



# class InstructorSerializer(serializers.ModelSerializer):
#     courses = CourseSerializer(many=True , read_only=True)
#     id = serializers.ReadOnlyField()
#     class Meta:
#         model = Instructor
#         fields = '__all__'

# Model Serializer End Here :- 



# hyper linked Model Serializer start here

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Courses
        fields = '__all__'

class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many=True , read_only=True ,
    view_name = 'courses-detail')

    class Meta:
        model = Instructor
        fields = '__all__'

# hyper linked model serializer end here