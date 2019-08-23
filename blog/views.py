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

from datetime import timezone
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Post
# LoginFormを「ｒ」という名前でインポートし、名前の衝突を回避。
from .forms import LoginForm as r

# Create your views here.
def top_page(request):
    posts = Post.objects.all()
    return render(request, 'blog/top_page.html', {'posts': posts})

def page_under_construction(request):
    return render(request, 'blog/page_under_construction.html', {})

def login(request):
    return render(request, 'blog/login.html',{})


def PostForm(POST):
    pass

class indexView(TemplateView):
    posts = Post.objects.all()
    template_name = "blog/index.html"

class loginView(LoginView):
    """ 名前衝突を回避するために、以下をコメントアウトし、forms.pyからインポートしてきた
    LoginFormを使用します。
      """
    #form_class = forms.LoginForm
    form_class = r
    template_name = "blog/login.html"

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





