from django.db import models


# Create your models here.
class Hour(models.Model):
    hour = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.hour)