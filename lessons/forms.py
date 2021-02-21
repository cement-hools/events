import datetime

from django import forms
from django.contrib.admin import widgets
from django.contrib.auth import get_user_model
from django.forms import SelectDateWidget, DateInput, CheckboxSelectMultiple

from .models import Course, Attendance

User = get_user_model()


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


class AttendanceForm(forms.ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        self.students = kwargs.pop('students')
        self.lessons = kwargs.pop('lessons')
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['lesson'].queryset = self.lessons
        # events_unregistered_users = User.objects.exclude(id__in=users_id_list)
        self.fields['student'].queryset = self.students

    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
            'student': CheckboxSelectMultiple(),
        }