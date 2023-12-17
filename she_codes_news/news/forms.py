# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment
from django.utils import timezone

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
            'pub_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]