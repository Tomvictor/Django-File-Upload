from django import forms
from mysite.models import drive

class UploadForm(forms.ModelForm):
    class Meta:
        model = drive
        fields = ["file"]
