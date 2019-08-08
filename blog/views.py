from django.shortcuts import render


# Create your views here.


def top_page(request):
    return render(request, 'blog/top_page.html', {})

def page_under_construction(request):
    return render(request, 'blog/page_under_construction.html', {})

def login(request):
    return render(request, 'blog/login.html',{})