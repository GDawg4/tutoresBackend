from rest_framework import viewsets
from day_hour.models import DayHour
from day_hour.serializers import DayHourSerializers

from permissions.services import APIPermissionClassFactory

class DayHourViewSet(viewsets.ModelViewSet):
    queryset = DayHour.objects.all()
    serializer_class = DayHourSerializers
    permission_classes = (
        APIPermissionClassFactory(
            name='CoursePermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': 'courses.delete_course',
                    'update': 'courses.change_course',
                    'partial_update': 'courses.change_course',
                }
            }
        ),
    )