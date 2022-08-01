from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
# Creating Class based View to render Registraton template and getting data using default User
# Registration Form class
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name= 'register.html'
    success_url = reverse_lazy('login')


