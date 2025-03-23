from django import forms
from .models import ShipingAddress


from django import forms
from .models import ShipingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}), 
        required=True
    )
    shipping_email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), 
        required=True
    )
    shipping_address1 = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}), 
        required=True
    )
    shipping_address2 = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2'}), 
        required=False
    )
    shipping_city = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), 
        required=True
    )
    shipping_state = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State/Province'}), 
        required=False
    )
    shipping_zipcode = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip/Postal Code'}), 
        required=True
    )
    shipping_country = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), 
        required=True
    )

    class Meta:
        model = ShipingAddress
        fields = [
            'shipping_full_name', 'shipping_email', 'shipping_address1',
            'shipping_address2', 'shipping_city', 'shipping_state', 
            'shipping_zipcode', 'shipping_country'  # Removed the extra space here
        ]
        exclude = ['user']


class PaymentForm(forms.Form):
    card_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card name'}), 
        required=True
    )
    card_number = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card number'}), 
        required=True
    )
    card_exp_date = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card exp-date'}), 
        required=True
    )
    card_cvv_number = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card cvv'}), 
        required=True
    )
    card_address1 = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card address1'}), 
        required=True
    )
    card_address2 = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card address2'}), 
        required=False
    )
    card_city = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card city'}), 
        required=True
    )
    card_state = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}), 
        required=False
    )
    card_zipcode = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zipcode'}), 
        required=True
    )
    card_country = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), 
        required=True
    )

