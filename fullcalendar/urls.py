from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    url('^calendar', views.calendar, name='calendar'),
    url('^add_event$', views.add_event, name='add_event'),
    url('^update$', views.update, name='update'),
    url('^remove', views.remove, name='remove'),
]
