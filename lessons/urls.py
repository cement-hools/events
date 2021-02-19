from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers_profile/', views.teachers_profile, name='teachers_profile'),
]
