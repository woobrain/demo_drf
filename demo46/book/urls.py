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
from rest_framework.routers import SimpleRouter,DefaultRouter
from book import views_serializer,views_apiview,views_genericapiview,view_modelmixin,\
    view_modelmixinchild,view_viewset,view_modelviewset
from . import views

urlpatterns = [
    # url(r'^$', views.IndexView.as_view()),
    # url(r'^books/$', views.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    # url(r'^books/$', views_serializer.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_serializer.BookView.as_view()),
    #
    # url(r'^heros/$', views_genericapiview.HeroView.as_view()),
    # url(r'^heros/(?P<pk>\d+)/$', views_genericapiview.HeroView.as_view()),
    #
    # url(r'^books/$', views_apiview.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_apiview.BookView.as_view()),
    #
    # url(r'^books/$', views_genericapiview.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_genericapiview.BookView.as_view()),

    # url(r'^books/$', view_modelmixin.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', view_modelmixin.BookView.as_view()),
    # url(r'^books/$', view_modelmixinchild.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', view_modelmixinchild.BookView.as_view()),
    # url(r'^books/last_book/$',view_modelviewset.BooksView.as_view({'get':'last_book'})),
    # url(r'^books/(?P<pk>\d+)/bread_book/$',view_modelviewset.BooksView.as_view({'get':'bread_book'}))
    # url(r'^books/$', view_modelviewset.BooksView.as_view({'get':'list','post':'create'})),
    # url(r'^books/(?P<pk>\d+)/$', view_modelviewset.BooksView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]
router = SimpleRouter()
router.register('books',view_modelviewset.BooksView,base_name='books')
print(router.urls)
urlpatterns += router.urls

