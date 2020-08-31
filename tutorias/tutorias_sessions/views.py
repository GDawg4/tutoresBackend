from rest_framework import viewsets

from tutorias_sessions.models import TutoriasSessions
from tutorias_sessions.serializers import TutoriasSessions

class SessionViewSet(viewsets.ModelViewSet):
    queryset = TutoriasSessions
    serializer_class = TutoriasSessions

