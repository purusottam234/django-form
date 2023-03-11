from django import forms
from .models import Contact


class MyForm(forms.Form):
    name = forms.CharField(max_length=100, label='your name')
    email = forms.EmailField(label='your email')
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
