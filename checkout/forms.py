from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('fullname', 'email', 'phonenumber',
                  'streetaddress1', 'streetaddress2',
                  'city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'fullname': 'Full Name',
            'email': 'Email Address',
            'phonenumber': 'Phone Number',
            'postcode': 'Postal Code',
            'city': 'Town or City',
            'streetaddress1': 'Street Address 1',
            'streetaddress2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['fullname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
