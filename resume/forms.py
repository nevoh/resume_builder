from django import forms

from .models import Education, Experience, Achievement, Language, Skill
from .widgets import DatePickerInput


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ['name', 'degree', ]


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ['title', 'company', 'start_date',
                  'end_date', 'description', ]

        widgets = {
            'start_date': DatePickerInput(),
            'end_date': DatePickerInput(attrs={
                'id': "end_date", }),
        }


class AchievementForm(forms.ModelForm):

    class Meta:
        model = Achievement
        fields = ['title', 'description', 'year', ]


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ['title', 'level', ]


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ['title', ]
