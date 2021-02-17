from django.shortcuts import render, get_object_or_404

from .models import Lesson, Student


def index(request):
    student = get_object_or_404(Student, user=request.user)
    print(student)
    students_lessons = student.course.lessons.all()
    lesson_arr = []
    for lesson in students_lessons:
        lesson_sub_arr = {}
        lesson_sub_arr['title'] = lesson.title
        lesson_sub_arr['start'] = str(lesson.start_date)
        lesson_sub_arr['end'] = str(lesson.end_date)
        lesson_arr.append(lesson_sub_arr)
    context = {'lessons': lesson_arr}
    return render(request, 'index.html', context)
