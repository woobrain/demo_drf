import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from book.model_serializers import HeroInfoSerializers
from book.models import BookInfo, HeroInfo
from book.serializers import BookSerializer


class BooksView(View):
    """
        获取所有图书和保存图书
    """

    def get(self, request):
        # 1、查询图书表获取取所有图书信息
        books = BookInfo.objects.all()
        # 2、返回图书信息
        # 2-1、初始化序列化器生成序列化器对象,将需要返回的数据对象传递进去,如果是查询集数据，包含多个数据对象，需要使用many=True
        ser = BookSerializer(books, many=True)
        # 2-2 data方法获取序列化后的结果
        return JsonResponse({'books': ser.data})

    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据 初始化序列化器对象，将前端需要验证的数据传递给data参数
        ser = BookSerializer(data=data_dict)
        # 2-2 执行验证方法
        ser.is_valid()
        # 2-3 获取验证后的状态信息
        if ser.errors:
            return JsonResponse({'errors': ser.errors})
        # 2-4 获取验证成功后的数据
        validated_data = ser.validated_data
        # 3、保存数据
        # 调用序列器中的create方法完成保存
        ser.save()
        # 4、返回结果
        return JsonResponse(ser.data)


class BookView(View):
    """
        获取单一图书
        更新
        删除
    """

    def get(self, request, pk):
        # 1、根据pk查询图书
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({"error": "图书不存在"})
        # 2、返回图书信息
        book = BookSerializer(book)
        return JsonResponse(book.data)

    def put(self, request, pk):
        # 1、获取更新图书
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({"error": "图书不存在"})
        # 2、获取更新字段数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 3、验证数据

        # 4、更新数据
        book_update = BookSerializer(book, data=data_dict)
        try:
            book_update.is_valid(raise_exception=True)
        except:
            return JsonResponse({'errors': book_update.errors})
        # 1.抛出异常的方法
        # if book_update.errors:
        #     return JsonResponse({'errors':book_update.errors})
        # 重新获取更新后的数据
        book_update.save()
        # 5、返回结果
        return JsonResponse(book_update.data)

    def delete(self, request, pk):
        # 1、获取删除对象
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({"error": "图书不存在"})
        # 2、逻辑删除
        book.is_delete = True
        book.save()
        return JsonResponse({})


class HeroView(View):
    def get(self, request, pk):
        try:
            hero = HeroInfo.objects.get(id=pk)
        except:
            return JsonResponse({"error": "图书不存在"})
        ser = HeroInfoSerializers(hero)

        return JsonResponse(ser.data)

    def put(self, request, pk):
        try:
            hero = HeroInfo.objects.get(id=pk)
        except:
            return JsonResponse({"error": "图书不存在"})
        data = json.loads(request.body.decode())
        ser = HeroInfoSerializers(hero, data=data)
        ser.is_valid()
        if ser.errors:
            return JsonResponse({"error": ser.errors})
        ser.save()
        return JsonResponse(ser.data)
