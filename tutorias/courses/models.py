from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)

    def __str__(self):
        return 'Course: {}'.format(self.name)