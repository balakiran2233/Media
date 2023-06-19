"""Socialmediaproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.articleList,name='article_list'),
    path('<id>/<slug>',views.articleDetail,name='article_detail'),
    path('article_create/',views.article_create,name='article_create'),
    path('login/',views.loginView,name='loginView'),
    path('logout/',views.logoutView,name='logoutView'),
    path('register/',views.registerView,name='registerview'),
    path('like_article/',views.like_article,name='like_article'),
    path('article_edit/<id>',views.article_edit,name='article_edit'),
    path('article_delete/<id>',views.article_delete,name='article_delete'),
    path('favourite_article/<id>',views.favourite_article,name='favourite_article'),
    path('favourites',views.article_favourite_list,name='article_favourite_list')
]
