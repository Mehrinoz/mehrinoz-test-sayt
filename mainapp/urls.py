from django.urls import path
from . import views
from .views import index, test_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('kitoblar/', views.book_list, name='books'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register, name='register'),
    path('tests/', test_list, name='test_list'),
    path('tests/<int:test_id>/', views.test_detail, name='test_detail')
]


