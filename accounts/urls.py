from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginView.as_view(), name="login"),
    path('logout/', views.logoutView.as_view(), name="logout"),
    path('index/',views.indexView.as_view(), name="index"),
    ]