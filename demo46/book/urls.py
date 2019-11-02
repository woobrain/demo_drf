"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from book import views_serializer
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    # url(r'^books/$', views.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    url(r'^books/$', views_serializer.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views_serializer.BookView.as_view()),

    url(r'^heros/$', views_serializer.HeroView.as_view()),
    url(r'^heros/(?P<pk>\d+)/$', views_serializer.HeroView.as_view()),
]