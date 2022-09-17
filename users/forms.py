from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import AttendanceIn, AttendanceOut, Profile, Skill, Message, Worklog, AttendanceIn, AttendanceOut, PersonalMeeting
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 
            'email', 
            'username', 
            'location', 
            'short_intro', 
            'bio', 
            'profile_image',
            'social_github',
            'social_twitter',
            'social_linkedin',
            'social_youtube',
            'social_website'
            ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class PersonalMeetingForm(ModelForm):
    class Meta:
        model = PersonalMeeting
        fields = ['name', 'email', 'title', 'meeting_link']

    def __init__(self, *args, **kwargs):
        super(PersonalMeetingForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class WorklogForm(ModelForm):
    class Meta:
        model = Worklog
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(WorklogForm, self).__init__(*args, **kwargs)

        self.fields['date'] = forms.DateField(widget=DatePickerInput)
        self.fields['start_time'] = forms.TimeField(widget=TimePickerInput)
        self.fields['worklog'].widget.attrs.update({'class': 'input'})
        self.fields['end_time'] = forms.TimeField(widget=TimePickerInput)
            
            
class AttendanceInForm(ModelForm):
    class Meta:
        model = AttendanceIn
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(AttendanceInForm, self).__init__(*args, **kwargs)

        self.fields['in_date'] = forms.DateField(widget=DatePickerInput)
        self.fields['in_time']= forms.TimeField(widget=TimePickerInput)

class AttendanceOutForm(ModelForm):
    class Meta:
        model = AttendanceOut
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(AttendanceOutForm, self).__init__(*args, **kwargs)

        self.fields['out_date'] = forms.DateField(widget=DatePickerInput)
        self.fields['out_time']= forms.TimeField(widget=TimePickerInput)