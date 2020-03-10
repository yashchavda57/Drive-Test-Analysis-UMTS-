from django import forms
from .models import DriveTestData

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DriveTestData
        fields = ('filename', 'file', )
