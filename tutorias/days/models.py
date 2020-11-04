from django.db import models


# Create your models here.
class Day(models.Model):
    day = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return '{}'.format(self.day)