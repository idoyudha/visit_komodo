from django import forms
from .models import Blog 
from ckeditor.widgets import CKEditorWidget


class BlogForm(forms.ModelForm):
    class Meta:
        content = forms.CharField(widget=CKEditorWidget())
        model = Blog
        fields = ['title', 'short_description', 'image_url', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3 }),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
        }