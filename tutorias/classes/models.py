from django.db import models


class Classes(models.Model):
    time_stamp = models.DateTimeField()
    teacher = models.ForeignKey('tutors.Tutor', on_delete=models.CASCADE)
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    def __str__(self):
        return 'Class: {} {} {}'.format(self.teacher, self.student, self.course)