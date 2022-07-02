from django import forms
from .models import Post, Category

choices = [cat for cat in Category.objects.all().values_list('name', 'name')]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'summary', 'content', 'pub_date', 'author', 'thumbnail')
        widgets = {
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden', 'id': 'userName'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'summary', 'content', 'pub_date', 'thumbnail')
        widgets = {
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
