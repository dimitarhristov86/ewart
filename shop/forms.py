from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Order


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50, label='Full name')
    subject = forms.CharField(max_length=250, label='Subject')
    email_address = forms.EmailField(required=True, max_length=150, label='Email address')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label='Message')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='This field is required!')
    email = forms.EmailField(help_text='This field is required!')
    password1 = forms.CharField(max_length=50, label='Password', help_text="Must be at least 8 characters long! ",
                                widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(max_length=50, label='Confirm Password', help_text='Must be the same as Password* field! ',
                                widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {'username': None}


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'address', 'image']


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
