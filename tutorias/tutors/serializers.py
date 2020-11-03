from rest_framework import serializers

from tutors.models import Tutor
from users.models import User
from users.serializers import UserSerializer
from courses.models import Course
from courses.serializers import CourseSerializer


class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Tutor
        fields = (
            'id',
            'user',
            'course',
            'hours'
        )
