from django.db import models

from tutors.models import Tutor
from users.models import User


# Create your models here.
class TutoriasSessions(models.Model):
    start = models.DateTimeField(auto_now=False)
    end = models.DateTimeField(auto_now=False)
    tutor = models.ForeignKey(
        'tutors.Tutor',
        on_delete=models.SET_NULL,
        null=True
    )
    student = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True
    )
    topic = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)