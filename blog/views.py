from django.shortcuts import render
# Create your views here.


def top_page(request):
    return render(request, 'blog/top_page.html', {})

