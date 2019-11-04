from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from book.models import BookInfo
from book.views_serializer import BookSerializer

class BooksView(ModelViewSet):

    serializer_class = BookSerializer
    queryset = BookInfo.objects.all()

    @action(methods=['get'],detail=False)
    def last_book(self,request):
        book = BookInfo.objects.latest('id')

        ser = self.get_serializer(book)

        return Response(ser.data)

    @action(methods=['get'],detail=True)
    def bread_book(self,request,pk):
        # 传什么id就取出什么
        # book = self.get_object()
        try:
            book = BookInfo.objects.filter(bread=pk)
        except:
            return Response({})

        ser = self.get_serializer(book,many=True)

        return Response(ser.data)