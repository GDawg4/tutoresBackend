from rest_framework import viewsets

from tutorias_sessions.models import TutoriasSessions
from tutorias_sessions.serializers import SessionsSerializers


class SessionViewSet(viewsets.ModelViewSet):
    queryset = TutoriasSessions.objects.all()
    serializer_class = SessionsSerializers

