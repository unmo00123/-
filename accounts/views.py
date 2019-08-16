from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from django.utils import timezone
from .models import Post


class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "blog/login.html"

class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "blog/logout.html"

class indexView(TemplateView):
    template_name = "blog/index.html"

def index(request):
    posts = Post
    render(request,"blog/index.html",{'posts': posts})