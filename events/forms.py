from django import forms

from .models import Event


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
