from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput,
                                help_text='Introduceti minim 8 caractere',
                                label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput,
                                help_text='Introduceti aceeasi parola ca mai sus',
                                label='Confirm Password')
    username = forms.CharField(help_text='Userul ales sa aiba minim 4 caractere', widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

