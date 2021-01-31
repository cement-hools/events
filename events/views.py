from django.shortcuts import render, get_object_or_404, redirect

from .forms import EventForm
from .models import Event


def index(request):
    """Главная страница"""
    events = Event.objects.all()
    context = {'events': events}
    return render(request, "index.html", context)


def event_view(request, event_id):
    """Просмотр мероприятия"""
    event = get_object_or_404(Event, pk=event_id)
    bloсks = event.bloсks.all()
    # form = CommentForm(request.POST or None)
    context = {
        "event": event,
        "bloсks": bloсks,
        }
    return render(request, "event.html", context)


def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, "new_event.html", {"form": form, "event": event})