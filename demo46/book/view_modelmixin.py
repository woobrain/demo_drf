import json

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from book.model_serializers import HeroInfoSerializers
from book.models import BookInfo, HeroInfo
from book.serializers import BookSerializer
from book.model_serializers import HeroInfoSerializers


class BooksView(GenericAPIView,CreateModelMixin,ListModelMixin):
    """
        获取所有图书和保存图书
    """
    serializer_class = BookSerializer
    queryset = BookInfo.objects.all()

    def get(self, request):
        # 1、查询图书表获取取所有图书信息
       return self.list(request)

    def post(self, request):

        return self.create(request)

class BookView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    """
        获取单一图书
        更新
        删除
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):

        return self.update(request)
    def delete(self, request, pk):
        # 1、获取删除对象
        return self.destroy(request)


class HeroView(GenericAPIView):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroInfoSerializers

    def get(self, request, pk):
        hero = self.get_object()
        ser = self.get_serializer(hero)

        return Response(ser.data)

    def put(self, request, pk):
        hero = self.get_object()
        data = request.data
        ser = self.get_serializer(hero, data=data)
        ser.is_valid()
        if ser.errors:
            return Response({"error": ser.errors})
        ser.save()
        return Response(ser.data)
