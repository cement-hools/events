from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:event_id>/', views.event_view, name="event"),
    path("<int:event_id>/edit/", views.event_edit,
         name="event_edit"),
    path("<int:event_id>/booking/", views.add_booking,
         name="event_booking"),

]
