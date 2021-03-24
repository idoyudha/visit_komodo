from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Blog 

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }