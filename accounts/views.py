from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms

class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "blog/login.html"

class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "blog/logout.html"

class indexView(TemplateView):
    template_name = "blog/index.html"