from django.urls import path, re_path, include
from . import views

app_name = 'user_infos'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('', views.logout, name='logout'),
]
