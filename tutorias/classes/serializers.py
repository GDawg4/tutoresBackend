from rest_framework import serializers

from classes.models import Classes

class ClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = (
            'time_stamp',
            'teacher',
            'student',
            'course'
        )