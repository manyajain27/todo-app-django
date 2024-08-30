from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['heading','description','due','category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter task description...'}),
            'due': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'category': forms.Select(attrs={'class': 'form-control'}) 
        }
        labels = {
            'heading': 'Task Title',
            'description': 'Task Description',
            'due': 'Due Date & time',
            'category': 'Category'
        }
        help_texts = {
            
        }
        error_messages = {
            'heading': {
                'max_length': 'The title is too long. Please keep it under 200 characters.',
            },
        }