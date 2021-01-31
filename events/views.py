from django.shortcuts import render

from .models import Event


def index(request):
    """Главная страница"""
    events = Event.objects.all()
    context = {'events': events}
    return render(request, "index.html", context)
