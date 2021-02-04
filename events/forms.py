from django import forms
from django.contrib.auth import get_user_model
from django.forms import CheckboxSelectMultiple

from .models import Event, Booking, EventBloсk

User = get_user_model()


class EventForm(forms.ModelForm):
    """Форма создания и релактирования мероприятия."""
    class Meta:
        model = Event
        fields = ("title", "description",)


class BookingForm(forms.ModelForm):
    """Форма регистрации пользователя на блоки мероприятия."""
    def __init__(self, *args, **kwargs):
        self.event_id = kwargs.pop('event_id')
        self.user = kwargs.pop('user')
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['block'].queryset = EventBloсk.objects.filter(
            event=self.event_id)
        self.fields['user'].initial = self.user

    class Meta:
        model = Booking
        fields = ('block', 'user')
        widgets = {
            'block': CheckboxSelectMultiple(),
        }
