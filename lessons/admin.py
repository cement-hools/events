from django.contrib import admin

from .models import Course, Lesson, LessonsType, Student, Attendance

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonsType)
admin.site.register(Student)
admin.site.register(Attendance)
