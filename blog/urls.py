from django.urls import path
from . import views





urlpatterns = {
    path('', views.top_page, name='top_page'),
    path('page_under_construction/', views.page_under_construction, name='page_under_construction'),
    path('login/', views.login, name='login'),
}
