from django.shortcuts import render,redirect
from .forms import MusicianForm
from .import models,forms
from .forms import MusicianForm
from .models import MusicianModel



def Musicians(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Musicians') 
    else:
        form = MusicianForm()
    return render(request, 'musician.html', {'form': form})


def Edit_musicians(request,id):
    musicians = models.MusicianModel.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musicians)
    if request.method=='POST':
        musician_form = forms.MusicianForm(request.POST,instance=musicians)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('Musicians')
    
    return render(request,'musician.html',{'form': musician_form})

def delete_musicians(request,id):
    Musician = models.MusicianModel.objects.get(pk=id)
    Musician.delete()
    return redirect('Musicians')