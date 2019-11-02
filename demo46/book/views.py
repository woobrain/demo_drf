

import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from book.models import BookInfo


# Create your views here.
class IndexView(View):
    def get(self, request, version):
        if version == '1.0':

            book = BookInfo.objects.get(id=3)
            data = {
                'title': book.btitle
            }
            return render(request, 'index.html', data)
        elif version == '2.0':
            pass
        else:
            pass

            # 分离模式
            # return JsonResponse(data)


class BooksView(View):
    """
        获取所有图书和保存图书
    """

    def get(self, request):
        # 1、查询图书表获取取所有图书信息
        books = BookInfo.objects.all()
        # 2、返回图书信息
        book_list = []
        for book in books:
            book_list.append(
                {
                    'id': book.id,
                    'btitle': book.btitle,
                    'bread': book.bread,
                    'bpub_date': book.bpub_date,
                    'bcomment': book.bcomment,
                }
            )
        return JsonResponse({'books': book_list})

    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        if len(data_dict['btitle']) >= 20 or len(data_dict['btitle']) <= 4:
            return JsonResponse({'error': '书名长度不符合'}, status=400)
        # 3、保存数据
        book = BookInfo.objects.create(**data_dict)
        # 4、返回结果
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bread': book.bread,
            'bpub_date': book.bpub_date,
            'bcomment': book.bcomment,
        })


class BookView(View):
    """
        获取单一图书
        更新
        删除
    """

    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'error': '图书不存在'})
        return JsonResponse({'id': book.id,
                             'btitle': book.btitle,
                             'bread': book.bread,
                             'bpub_date': book.bpub_date,
                             'bcomment': book.bcomment, })

    def put(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'error': '图书不存在'})
        data_dict = json.loads(request.body.decode())
        res = BookInfo.objects.filter(id=pk).update(**data_dict)
        if res == 0:
            return JsonResponse({'error': '更新失败'})
        book = BookInfo.objects.get(id=pk)

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bread': book.bread,
            'bpub_date': book.bpub_date,
            'bcomment': book.bcomment,
        })

    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'error': '图书不存在'})
        book.is_delete = True

        return JsonResponse({})
