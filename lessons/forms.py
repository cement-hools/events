import datetime

from django import forms
from django.contrib.admin import widgets
from django.forms import SelectDateWidget, DateInput

from .models import Course


class CourseForm(forms.ModelForm):
    # start_date = forms.DateField(required=False, widget=DateInput(
    #     attrs={'type': 'datetime-local'}), localize=True)

    class Meta:
        model = Course
        fields = '__all__'
        # labels = {
        #     "text": "Введите текст",
        #     "group": "Выберите группу",
        #     "image": "Изображение"
        # }
        # help_texts = {
        #     "text": "Текст поста",
        #     "group": "Из уже существующих",
        #     "image": "Выберите изображение"
        # }

        # widgets = {
        #     'publish_date': widgets.AdminDateWidget,
        #     'publish_time': widgets.AdminTimeWidget,
        #     'publish_datetime': widgets.AdminSplitDateTime,
        # }