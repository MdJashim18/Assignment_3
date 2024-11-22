from django.shortcuts import render
from .forms import contactForm
# Create your views here.
def home(request):
    print(request.POST)
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # file_path = './first_app/upload/' + file.name
            # with open(file_path, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
        # return render(request,'djangoForm.html',{'form' : form})
    else:
        form = contactForm()
    
    return render(request,'home.html',{'form' : form})
