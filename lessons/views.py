from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CourseForm, AttendanceForm
from .models import Student, Course, Lesson, Attendance

User = get_user_model()


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


def admins_profile(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'admins_profile.html', context)


def new_course(request):
    """Создание нового курса"""
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admins_profile')
    return render(request, 'new_course.html', {'form': form})


def course_edit(request, course_id):
    """Редактировать курс."""
    course = get_object_or_404(Course, pk=course_id)
    form = CourseForm(request.POST or None, instance=course)

    context = {'form': form, 'course': course}
    if form.is_valid():
        form.save()
        return redirect('admins_profile')
    return render(request, "new_course.html", context)


def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('admins_profile')


def course_view(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    students = Student.objects.filter(course__id=course_id)
    attendance = Attendance.objects.all()
    context = {
        'course': course,
        'lessons': lessons,
        'students': students,
        'attendance': attendance,
    }
    return render(request, "course_view.html", context)


def attendance(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    course_id = lesson.course.id
    students = lesson.course.students.all()
    students_id = [student.user.id for student in students]
    students_user = User.objects.filter(id__in=students_id)

    form = AttendanceForm(request.POST,
                          lesson=lesson,
                          students=students_user,
                          )
    print('hi')
    if form.is_valid():
        form.save()
        print("created")
        return redirect("course_view", course_id=course_id)
    return render(request, "attendance.html",
                  {"form": form, 'course_id': course_id,
                   'lesson_id': lesson_id, })


def attendance_edit(request, lesson_id):
    attendance = get_object_or_404(Attendance, lesson=lesson_id)
    print(attendance, lesson_id)
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    students = lesson.course.students.all()
    students_id = [student.user.id for student in students]
    students_user = User.objects.filter(id__in=students_id)
    form = AttendanceForm(request.POST or None,
                          lesson=lesson,
                          students=students_user,
                          instance=attendance,
                          # initial={'student': students_user}
                          )
    if form.is_valid():
        form.save()
        print("created_edit")
        return redirect("course_view", course_id=lesson.course.id)
    return render(request, "attendance.html",
                  {"form": form, 'course_id': lesson.course.id,
                   'lesson_id': lesson_id, })
