from .models import Task
from django.forms import ModelForm,Textarea,TextInput


class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['title','task']
        widgets={
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter name of your task'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
        }
