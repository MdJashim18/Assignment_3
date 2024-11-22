from django.shortcuts import render,redirect
from .import forms 
# Create your views here.

def categories(request):
    if request.method=='POST':
        form = forms.Category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = forms.Category_form()
    return render(request,'category.html',{'form' : form})