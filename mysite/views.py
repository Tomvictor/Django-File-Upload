from django.shortcuts import render
from .forms import UploadForm

# Create your views here.


def home(request):
    context = {
        "form":UploadForm
    }
    return render(request,'home.html',context)
