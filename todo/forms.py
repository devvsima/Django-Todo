from django import forms
from django.forms import ModelForm
from .models import TodoList

class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'content', 'due_date', 'image']
        
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Введите название'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Введите описание'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    due_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
        'type': 'date'
    }))
