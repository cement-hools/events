from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers_profile/', views.teachers_profile, name='teachers_profile'),
    path('students_profile/', views.students_profile, name='students_profile'),
    path('admins_profile/', views.admins_profile, name='admins_profile'),
    path('new_course/', views.new_course, name='new_course'),
    path('<int:course_id>/edit/', views.course_edit, name='course_edit'),
    path('<int:course_id>/delete/', views.course_delete, name='course_delete'),
    path('course/<int:course_id>/', views.course_view, name='course_view'),
    path('course/<int:course_id>/add_students/',
         views.add_students_on_course, name='add_students_on_course'),
    path('course/<int:course_id>/new_lesson/',
         views.new_lesson, name='new_lesson'),

    path('user/<int:user_id>/remove_from_the_course/',
         views.remove_from_the_course, name='remove_from_the_course'),
    path('lesson/<int:lesson_id>/edit',
         views.lesson_edit, name='lesson_edit'),
    path('lesson/<int:lesson_id>/delete',
         views.lesson_delete, name='lesson_delete'),

    path('lesson/<int:lesson_id>/attendance/',
         views.attendance, name='attendance'),

]
