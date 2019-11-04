import json

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from book.model_serializers import HeroInfoSerializers
from book.models import BookInfo, HeroInfo
from book.serializers import BookSerializer
from book.model_serializers import HeroInfoSerializers


class BooksView(ListCreateAPIView):
    """
        获取所有图书和保存图书
    """
    serializer_class = BookSerializer
    queryset = BookInfo.objects.all()


class BookView(RetrieveUpdateDestroyAPIView):
    """
        获取单一图书
        更新
        删除
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer


class HeroView(GenericAPIView):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroInfoSerializers
