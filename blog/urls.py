from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('page_under_construction/', views.page_under_construction, name='page_under_construction'),
    path('create/',views.CreateView.as_view(),name="create"),
    path('index/',views.indexView.as_view(), name="index"),
    path('login/', views.loginView.as_view(), name="login"),
    path('logout/', views.logoutView.as_view(), name="logout"),
]
