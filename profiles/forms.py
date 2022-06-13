from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for the UserProfile
    """
    class Meta:
        model = UserProfile()
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phonenumber': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_city': 'Town or City',
            'default_streetaddress1': 'Street Address 1',
            'default_streetaddress2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phonenumber'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
