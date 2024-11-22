from django import forms 
from django.core import validators
from task.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',  
                    'class': 'form-control', 
                    'placeholder': 'YYYY-MM-DD',
                }
            ),
            'description' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : '4',
                    'placeholder' : 'Enter your description',
                }
            ),
            'categories': forms.SelectMultiple(  
                attrs={
                    'class': 'form-control',
                }
            ),
        }