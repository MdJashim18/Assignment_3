from django import forms 
from django.core import validators
from django.forms.widgets import NumberInput
import datetime
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ('yellow', 'Yellow'),
    ('white', 'White'),
]
# MyModel = [
#     ('1','Logo design'),
#     ('2','Domain Selection'),
# ]


class contactForm(forms.Form):
    name = forms.CharField(initial='Your name',)
    email = forms.EmailField(label="Please enter your email address",)
    comment = forms.ChoiceField(widget=forms.Textarea(attrs={'rows' : 3}))
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(max_length=100)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.ChoiceField(widget=forms.RadioSelect , choices=FAVORITE_COLORS_CHOICES)
    favorite_colorss = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colorsss = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    #model_choice = forms.ModelChoiceField(queryset = MyModel.objects.all(),initial = 0)
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='File Extention must be ended with "pdf"')])
    Appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))