
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
)
from .models import Contact
from .forms import ContactForm



class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy('index:home')