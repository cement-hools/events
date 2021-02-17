from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class LessonsType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='lessons')
    description = models.TextField()
    type = models.ForeignKey(LessonsType, on_delete=models.SET_NULL,
                             related_name='lessons', null=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL,
                                related_name='lessons', null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='students')

    def __str__(self):
        return f'Студент {self.user} записан на "{self.course}"'
