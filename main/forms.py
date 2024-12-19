from django import forms
from .models import Task

class add_task(forms.ModelForm):
    class Meta:
        model = Task  # Link the form to the Task model
        fields = ['title', 'description', 'complete', 'priority']  # Specify fields to include
        labels = {
            'title': 'Task Name',
            'description': 'Description',
            'complete': 'Is Completed?',
            'priority': 'Its Priority:',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter task name'}),
            'description': forms.TextInput(attrs={'placeholder': 'Enter Detials about your task (Optional)'}),
        }