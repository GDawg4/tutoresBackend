from rest_framework import serializers
from days.models import Day

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['day']