from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50, label='Full name')
    subject = forms.CharField(max_length=250, label='Subject')
    email_address = forms.EmailField(required=True, max_length=150, label='Email address')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label='Message')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']