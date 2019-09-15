from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import ContactModel

from django import forms
from .models import Post

class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['time']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'placeholder': 'Message'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')