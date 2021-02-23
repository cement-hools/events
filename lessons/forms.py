from django import forms
from django.contrib.auth import get_user_model
from django.forms import CheckboxSelectMultiple

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
        self.lesson = kwargs.pop('lesson')
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = self.students

    class Meta:
        model = Attendance
        fields = ('student',)
        widgets = {
            'student': CheckboxSelectMultiple(),
        }


class AddStudentOnCourseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('users')
        super(AddStudentOnCourseForm, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = self.users

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )