from rest_framework import serializers

from tutorias_sessions.models import TutoriasSessions

class SessionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TutoriasSessions
        fields = (
            'id',
            'start',
            'end',
            'tutor',
            'student',
            'topic',
            'rating'
        )