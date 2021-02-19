from django.shortcuts import render, get_object_or_404

from .models import Student, Course


def lessons_in_json(lessons):
    lesson_arr = []
    for lesson in lessons:
        lesson_sub_arr = dict()
        lesson_sub_arr['id'] = lesson.id
        lesson_sub_arr['title'] = lesson.title
        lesson_sub_arr['start'] = str(lesson.start_date)
        lesson_sub_arr['end'] = str(lesson.end_date)
        lesson_arr.append(lesson_sub_arr)
    return lesson_arr


def index(request):
    if request.user.is_authenticated:
        print('group: ', request.user.groups.all())
        return render(request, 'index.html', {})
    return render(request, 'index.html', {})

    student = get_object_or_404(Student, user=request.user)
    students_lessons = student.course.lessons.all()
    students_lessons_json = lessons_in_json(students_lessons)
    context = {'lessons': students_lessons_json}
    return render(request, 'index.html', context)


def teachers_profile(request):
    teacher = request.user
    teachers_lessons = teacher.lessons.all()
    teachers_lessons_json = lessons_in_json(teachers_lessons)
    teachers_lessons_id = [lesson.id for lesson in teachers_lessons]
    teachers_courses = Course.objects.filter(
        lessons__id__in=teachers_lessons_id).distinct()
    context = {
        'teachers_courses': teachers_courses,
        'teachers_lessons_json': teachers_lessons_json,
    }
    return render(request, 'teachers_profile.html', context)
