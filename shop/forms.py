from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50, label='Full name')
    subject = forms.CharField(max_length=250, label='Subject')
    email_address = forms.EmailField(required=True, max_length=150, label='Email address')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label='Message')
