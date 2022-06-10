from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
    NewsletterForm to sign up for the newsletter
    """
    class Meta:
        model = Newsletter
        fields = '__all__'
