from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from book.models import BookInfo
from book.views_serializer import BookSerializer


class SetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 3


class BooksView(ModelViewSet):

    serializer_class = BookSerializer
    queryset = BookInfo.objects.all()
    pagination_class = SetPagination

    # authentication_classes = (SessionAuthentication, BasicAuthentication)

    # permission_classes = (IsAuthenticated,)

    # throttle_classes = (UserRateThrottle,)
    # filter_fields = ('btitle', 'bread','bcomment')

    # filter_backends = [OrderingFilter]
    # ordering_fields = ('id', 'bread', 'bpub_date','bcomment')

    @action(methods=['get'],detail=False)
    def last_book(self,request):
        """
            获取最后一本书
        :param request:
        :return:
        """
        # data = 1/0
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