from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from logbook.core.models import Entry, Category


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'slug', 'body', 'url', 'category',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'slug',)

