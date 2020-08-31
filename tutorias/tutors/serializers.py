from rest_framework import serializers

from tutors.models import Tutor
from users.models import User
from users.serializers import UserSerializer
from courses.models import Course
from courses.serializers import CourseSerializer


class TutorSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(many=False)
    course = CourseSerializer(many=False)

    class Meta:
        model = Tutor
        fields = (
            'id',
            'user_id',
            'course'
        )
