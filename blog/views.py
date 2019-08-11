from datetime import timezone
from django.shortcuts import render,redirect
from .models import CreateView

# Create your views here.

def top_page(request):
    return render(request, 'blog/top_page.html', {})

def page_under_construction(request):
    return render(request, 'blog/page_under_construction.html', {})

def login(request):
    return render(request, 'blog/login.html',{})


def PostForm(POST):
    pass


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index.html')
    else:
        form = PostForm()
    return render(request, 'blog/index.html', {'form': form})


