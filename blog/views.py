from django.shortcuts import render
from django.views.generic import TemplateView,CreateView # 追記
from django.contrib.auth.forms import UserCreationForm  # 追記
from django.urls import reverse_lazy # 追記


# Create your views here.

def top_page(request):
    return render(request, 'blog/top_page.html', {})

def page_under_construction(request):
    return render(request, 'blog/page_under_construction.html', {})

def login(request):
    return render(request, 'blog/login.html',{})

class createView(CreateView):
    form_class = UserCreationForm
    template_name = "blog/create.html"
    success_url = reverse_lazy("login")


