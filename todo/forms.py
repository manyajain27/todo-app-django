from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['heading','description','due','category','completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter task description...'}),
            'due': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'category': forms.TextInput(attrs={'rows':1,'placeholder':'enter category of task'})
        }
        labels = {
            'heading': 'Task Title',
            'description': 'Task Description',
            'due': 'Due Date & time',
            'category': 'Category'
        }
        help_texts = {
            'heading': 'Enter a brief title for your task.',
            'due': 'By when does this task need to be completed?'
        }
        error_messages = {
            'heading': {
                'max_length': 'The title is too long. Please keep it under 200 characters.',
            },
        }