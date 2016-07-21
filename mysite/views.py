from django.shortcuts import render
from .forms import UploadForm
from .models import drive
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            print(instance)
            instance.save()

    context = {
        "form":UploadForm
    }
    return render(request,'home.html',context)
