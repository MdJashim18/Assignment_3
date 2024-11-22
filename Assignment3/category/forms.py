from category.models import Category
from django import forms 


class Category_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        

