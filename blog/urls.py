from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('page_under_construction/', views.page_under_construction, name='page_under_construction'),
    path('login/', views.login, name='login'),
    path('create/',views.CreateView.as_view(),name="create"),
    path('test/',views.test,name="test"),
]
