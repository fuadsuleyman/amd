from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    num_title = forms.ChoiceField(widget = forms.Select(attrs={
                'class': 'form-control col-12',
                
            }) , 
                     choices = (
        [('050', '050'),
        ('051', '051'),
        ('055', '055'),
        ('070', '070'),
        ('077', '077'),
        ('099', '099'),]
    ), initial='---', required = True,)
   
    class Meta:
        model = Checkout
        fields = (
            'name',
            'surname',
            'email',
            'num_title',
            'tel_number',
            
        )

        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': 'form-control col-12',
                'placeholder': 'Ad '
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control col-12',
                'placeholder': 'Soyad '
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control ',
                'placeholder': 'E-posta adresiniz'
            }),
            'tel_number': forms.NumberInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Mobil nömrə'
            }),
            

        }