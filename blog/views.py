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
app_name='blog'

from datetime import timezone
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Post, Like
# LoginFormを「ｒ」という名前でインポートし、名前の衝突を回避。
from .forms import LoginForm as r
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def top_page(request):
    posts = Post.objects.all()
    like = Like.objects.all().filter(post_id=request.user.id)
    return render(request, 'blog/top_page.html', {'posts': posts, 'like': like})

def page_under_construction(request):
    return render(request, 'blog/page_under_construction.html', {})




def PostForm(POST):
    pass

def indexView(request):
    posts = Post.objects.all()
    like = Like.objects.all().filter(post_id=request.user.id)
    return render(request, 'blog/index.html', {'posts': posts, 'like': like})

class loginView(LoginView):
    """ 名前衝突を回避するために、以下をコメントアウトし、forms.pyからインポートしてきた
    LoginFormを使用します。
      """
    form_class = r
    template_name = "blog/login.html"
    reverse_lazy('login')



class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "blog/logout.html"

def post_new(request):
    # 以下のソースの意味は、データがPOSTデータで飛んできたときは、saveメソッドでデータを登録する処理です。
    # そして、データを登録しようとするときにだけ、posts = Post.objects.filter(published_date__lte=
    # timezone.now()).order_by('published_date')が稼働します。当然単純にページを表示させるときには
    # このif文の中は通りません。そのため、データが表示されませんでした。
    # 現在全体的な仕様としてはaccountsの中のviews.py(indexViewメソッド)を通しているように見受けられました。
    # 細かい設定（仕様）などが現状どうなっているのかわからなかったので、accounts.viewsでblog.modelsをimport
    # することができませんでした。
    # 要は、viewsでORマッパーを使用したDB処理を行い、その結果をフロントに返すことで対応できます。
    # そのため、今回のシステム仕様でいえばaccounts.viewsでblog.modelsをインポートしてきてORマッパーを記述し、
    # 取得データをフロントに返すことができれば一応目的は果たせると思います。が、出来ればディレクトリ構造は統一性、
    # 一貫性などをもたせることをおススメします。
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'blog/index.html', {'posts': posts})
    else:
        form = PostForm()
    return render(request, 'blog/index.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView as cf
from django.urls import reverse_lazy
class CreateView(cf):
    form_class = UserCreationForm
    template_name = "blog/create.html"
    success_url = reverse_lazy("login")



def like(requests):
    s = Like(
        post_id=requests.POST['post_id'],
        user_id=requests.POST['user_id'],
    )
    s.save()
    print(requests.POST['user_id'])
    print(requests.POST['post_id'])
    return redirect('index/')
