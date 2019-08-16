


from datetime import timezone
from django.shortcuts import render,redirect
from .models import CreateView, Post

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
            return render(request, 'blog/index.html', {'posts': posts})
    else:
        form = PostForm()
    return render(request, 'blog/index.html', {'form': form})





