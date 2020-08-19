from rest_framework import viewsets

from classes.models import Classes
from classes.serializers import ClassesSerializers

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializers