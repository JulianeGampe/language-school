from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    ContactForm to  contact the language school
    """
    class Meta:
        model = Contact
        fields = '__all__'
