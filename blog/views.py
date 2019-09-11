"""
エラーの原因は、
class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "blog/login.html"
の「form_class = forms.LoginForm」で、インポートしているのがfrom django import formsからのものだと認識をされていた点にあります。
いわゆる名前の競合が生じておりました。
これを解消するため、
from .forms import LoginForm as r
で　as文を使用して名前の衝突を回避しました。

"""
from django.contrib.auth.decorators import login_required

app_name='blog'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, Like
# LoginFormを「ｒ」という名前でインポートし、名前の衝突を回避。
from .forms import LoginForm as r
from .forms import PostForm

# Create your views here.
def top_page(request):
    return render(request, 'blog/top_page.html', {})

def page_under_construction(request):
    return render(request, 'blog/page_under_construction.html', {})



class loginView(LoginView):
    """ 名前衝突を回避するために、以下をコメントアウトし、forms.pyからインポートしてきた
    LoginFormを使用します。
      """
    form_class = r
    template_name = "blog/login.html"
    reverse_lazy('login')



class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "blog/logout.html"

@login_required
def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()

    posts = Post.objects.order_by('-created_date')[:5]
    like_count = Like.objects.count()
    return render(request,'blog/index.html', dict(posts=posts, like_count=like_count, form=form))

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView as cf
from django.urls import reverse_lazy

class CreateView(cf):
    form_class = UserCreationForm
    template_name = "blog/create.html"
    success_url = reverse_lazy("blog:login")


@login_required
def like(requests):
    if requests.method == 'POST':
        Like.objects.create()

    return redirect('blog:index')
