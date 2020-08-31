from django.db import models


class Classes(models.Model):
    time_stamp = models.DateTimeField()
    teacher = models.ForeignKey('tutors.Tutor', on_delete=models.CASCADE)
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    location = models.ForeignKey('classrooms.Classroom', on_delete=models.CASCADE, null=True)
    link = models.CharField(max_length=500, null=False, default='TBD')

    def __str__(self):
        return 'Class: {} {} {}'.format(self.teacher, self.student, self.course)