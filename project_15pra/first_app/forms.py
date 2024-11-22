from django import forms 
from first_app.models import StudentModel
from django.forms.widgets import NumberInput
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'btn-primary'}),
            'date_field': forms.DateInput(attrs={'type': 'date'}),
            'date_time_field': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        help_texts = {
            'name' : 'Write your full name'
        }
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }