from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from .models import Contact


class ContactForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)

    #     # add custom error messages
    #     self.fields['phone_number'].error_messages.update({
    #         'required': 'Please let us know what to call you!',
    #     })

    # phone_number = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': "form-control",
    #         'id': "review",
    #         'placeholder': "Əlaqə nomrəsini daxil edin",
    #         'required': True
    #     }),
    #     error_messages={'invalid': 'your custom error message'}
    # )

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].label = "name"
    #     self.fields['last_name'].label = "last-name"
    #     self.fields['phone_number'].label = "review"
    #     self.fields['email'].label = "email"
    #     self.fields['message'].label = "exampleFormControlTextarea1"

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'message'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "name",
                'placeholder': "Adıvızı daxil edin",
                'maxlength': 50,
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "last-name",
                'placeholder': "Soyadivızı daxil edin",
                'maxlength': 50,
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': "form-control",
                'id': "review",
                'placeholder': "Əlaqə nomrəsini daxil edin",
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'id': "email",
                'placeholder': "Elektron poçt ünvanınızı daxil edin",
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'id': "exampleFormControlTextarea1",
                'placeholder': "Mesajıvızı daxil edin...",
                'rows': 6,
                'required': True
            })

        }
        labels = {
            'first_name': 'Ad',
            'last_name': 'Soyad',
            'phone_number': 'Əlaqə nomrəsi',
            'email': 'Elektron poçt ünvanı',
            'message': 'Mesaj'
        }
        error_messages = {
            'phone_number': {
                # 'required': "This writer's name is too long.",
                'invalid': 'salam'
            },
        }
