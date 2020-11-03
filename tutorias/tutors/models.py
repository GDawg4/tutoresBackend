from django.db import models


class Tutor(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    course = models.ManyToManyField('courses.Course', related_name='tutors')
    hours = models.ManyToManyField('day_hour.DayHour', related_name='hours')

    def __str__(self):
        return 'Tutor: {}'.format(self.user_id)