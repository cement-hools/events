from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LessonsType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='lessons')
    description = models.TextField()
    type = models.ForeignKey(LessonsType, on_delete=models.SET_NULL,
                             related_name='lessons', null=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL,
                                related_name='lessons', null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='students')

    def __str__(self):
        return f'Студент {self.user} записан на "{self.course}"'


class Attendance(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    student = models.ManyToManyField(User, related_name='attendances',
                                     blank=True)
    # attendance = models.BooleanField()

    # def __str__(self):
    #     attendance = 'присутствовал' if self.attendance else 'не присутствовал'
    #     return f'Студент {self.student} {attendance} на уроке "{self.lesson}"'
