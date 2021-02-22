from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers_profile/', views.teachers_profile, name='teachers_profile'),
    path('admins_profile/', views.admins_profile, name='admins_profile'),
    path('new_course/', views.new_course, name='new_course'),
    path('<int:course_id>/edit/', views.course_edit, name='course_edit'),
    path('<int:course_id>/delete/', views.course_delete, name='course_delete'),
    path('course/<int:course_id>/', views.course_view, name='course_view'),
    path('lesson/<int:lesson_id>/attendance/',
         views.attendance, name='attendance'),
    path('lesson/<int:lesson_id>/attendance/edit',
             views.attendance_edit, name='attendance_edit'),
]
