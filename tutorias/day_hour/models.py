from django.db import models

# Create your models here.
class DayHour(models.Model):
    hour = models.ForeignKey(
        'hours.Hour',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    day = models.ForeignKey(
        'days.Day',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('hour', 'day')

    def __str__(self):
        return '{} {} horas'.format(self.day, self.hour)