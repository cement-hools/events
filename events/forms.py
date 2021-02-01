from django import forms
from django.forms import CheckboxSelectMultiple

from .models import Event, Booking, EventBloсk


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "description",)
        labels = {
            "title": "Введите текст",
            "description": "Выберите группу",
        }
        help_texts = {
            "title": "Текст поста",
            "description": "Из уже существующих",
        }


class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.event_id = kwargs.pop('event_id')
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['block'].queryset = EventBloсk.objects.filter(
            event=self.event_id)

    block = CheckboxSelectMultiple()

    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'block': CheckboxSelectMultiple(),
        }
