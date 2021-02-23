from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CourseForm, AttendanceForm, AddStudentOnCourseForm
from .models import Student, Course, Lesson, Attendance
from .my_functions import group_required, lessons_in_json

User = get_user_model()

GROUP_ADMIN = Group.objects.get(name='admin')
GROUP_TEACHER = Group.objects.get(name='teacher')
GROUP_STUDENT = Group.objects.get(name='student')


def index(request):
    """Главная страница."""
    if not request.user.is_authenticated:
        return render(request, 'index.html', {})
    print('group: ', request.user.groups.all())
    if request.user.groups.filter(name__in=['admin', ]).exists():
        print('gooood!!!!')
    return render(request, 'index.html', {})


@group_required(GROUP_STUDENT)
def students_profile(request):
    """Кабинет студента."""
    student = get_object_or_404(Student, user=request.user)
    students_lessons = student.course.lessons.all()
    students_lessons_json = lessons_in_json(students_lessons)
    context = {'lessons': students_lessons_json}
    return render(request, 'students_profile.html', context)


@group_required(GROUP_TEACHER)
def teachers_profile(request):
    """Кабинет учителя."""
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


@group_required(GROUP_ADMIN)
def admins_profile(request):
    """Кабинет админа."""
    if request.user.groups.filter(name__in=[GROUP_ADMIN]).exists():
        courses = Course.objects.all()
        context = {
            'courses': courses,
        }
        return render(request, 'admins_profile.html', context)
    return render(request, 'index.html', {})


@group_required(GROUP_ADMIN)
def new_course(request):
    """Создание нового курса"""
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admins_profile')
    return render(request, 'new_course.html', {'form': form})


@group_required(GROUP_ADMIN)
def course_edit(request, course_id):
    """Редактировать курс."""
    course = get_object_or_404(Course, pk=course_id)
    form = CourseForm(request.POST or None, instance=course)

    context = {'form': form, 'course': course}
    if form.is_valid():
        form.save()
        return redirect('admins_profile')
    return render(request, "new_course.html", context)


@group_required(GROUP_ADMIN)
def course_delete(request, course_id):
    """Удалить курс."""
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('admins_profile')


@group_required(GROUP_ADMIN)
def course_view(request, course_id):
    """Просмотр курса."""
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    students = Student.objects.filter(course__id=course_id)
    context = {
        'course': course,
        'lessons': lessons,
        'students': students,
    }
    return render(request, "course_view.html", context)


@group_required(GROUP_ADMIN)
def attendance(request, lesson_id):
    """Посещаемость урока."""
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    students = lesson.course.students.all()
    students_id = [student.user.id for student in students]
    students_user = User.objects.filter(id__in=students_id)

    attendance, created = Attendance.objects.get_or_create(lesson=lesson)

    form = AttendanceForm(request.POST or None,
                          lesson=lesson,
                          students=students_user,
                          instance=attendance,
                          )
    if form.is_valid():
        form.save()
        return redirect("course_view", course_id=lesson.course.id)
    return render(request, "attendance.html",
                  {"form": form, 'course_id': lesson.course.id,
                   'lesson_id': lesson_id, })


@group_required(GROUP_ADMIN)
def add_students_on_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    all_students = Student.objects.all()
    all_students_id = [student.user.id for student in all_students]
    users_are_not_students = User.objects.all().exclude(id__in=all_students_id)
    print(users_are_not_students)

    form = AddStudentOnCourseForm(request.POST or None,
                                  users=users_are_not_students,
                                  )

    if form.is_valid():
        users = form.cleaned_data['users']
        for user in users:
            Student.objects.create(user=user, course=course)
            user.groups.add(GROUP_STUDENT)

        return redirect("course_view", course_id=course_id)

    context = {
        'users_are_not_students': users_are_not_students,
        'course': course,
        'form': form
    }
    return render(request, "add_students_on_course.html", context)


@group_required(GROUP_ADMIN)
def remove_from_the_course(request, user_id):
    user = get_object_or_404(User, id=user_id)
    student = get_object_or_404(Student, user=user)
    course = student.course

    user.groups.remove(GROUP_STUDENT)
    student.delete()

    return redirect("course_view", course_id=course.id)
