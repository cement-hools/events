from django import forms
from django.contrib.auth import get_user_model
from django.forms import CheckboxSelectMultiple

from .models import Event, Booking, EventBloсk

User = get_user_model()


class EventForm(forms.ModelForm):
    """Форма создания и редактирования мероприятия."""

    class Meta:
        model = Event
        fields = ("title", "description",)


class BookingForm(forms.ModelForm):
    """Форма регистрации пользователя на блоки мероприятия."""

    def __init__(self, *args, **kwargs):
        self.event_id = kwargs.pop('event_id')
        super(BookingForm, self).__init__(*args, **kwargs)
        event_bloks_list = EventBloсk.objects.filter(event=self.event_id)
        self.fields['blocks'].queryset = event_bloks_list
        
        events_bokings = Booking.objects.filter(blocks__in=event_bloks_list)
        users_id_list = []
        for booking in events_bokings:
            users_id = [user.id for user in booking.users.all()]
            users_id_list.extend(users_id)
        events_unregistered_users = User.objects.exclude(id__in=users_id_list)
        self.fields['users'].queryset = events_unregistered_users

    class Meta:
        model = Booking
        fields = ('blocks', 'users')
        widgets = {
            'blocks': CheckboxSelectMultiple(),
            'users': CheckboxSelectMultiple(),
        }
