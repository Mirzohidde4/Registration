from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreate
from django.urls import reverse_lazy

# Create your views here.
class SignUp(CreateView):
    form_class = UserCreate
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'