from rest_framework import serializers
from day_hour.models import DayHour
from hours.serializers import HourSerializer
from days.serializers import DaySerializer

class DayHourSerializers(serializers.ModelSerializer):
    hour = serializers.StringRelatedField()
    day = serializers.StringRelatedField()

    class Meta:
        model = DayHour
        fields = (
            'hour',
            'day'
        )