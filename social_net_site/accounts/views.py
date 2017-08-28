from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import CreateView

# Create your views here.


class SignUp(CreateView):
    # ne kreiramo objkeat od kl;ase UserCreateForm, vec samo dodeljujemo form_class
    form_class = forms.UserCreateForm
    #Za uspesan login ide na login page, ceka se submit da bi nas odveo do login opet
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
