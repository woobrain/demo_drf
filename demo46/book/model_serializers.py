from rest_framework import serializers
from book.models import BookInfo,HeroInfo
from book.serializers import BookSerializer


class HeroInfoSerializers(serializers.ModelSerializer):

    # hbook = BookSerializer()
    hname = serializers.CharField(max_length=2,min_length=1)


    class Meta:
        model = HeroInfo
        # fields是得到那些字段,__all__是全部字段包括hbook
        # fields = '__all__'
        fields =('id','hname','hbook','hgender','hcomment')
        # 指明哪些字段只用序列化输出
        # read_only_fields = ('id','hname')
        # exclude是排除哪些字段
        # exclude = ('id',)
        # 添加额外参数
        extra_kwargs = {
            'hcomment':{'max_length':8,'required':True},
            'hname':{'max_length':3,'min_length':2,'required':True}
        }


# class BookInfoSerializers(serializers.ModelSerializer):
#
#     # hbook = BookSerializer()
#     btitle = serializers.CharField(max_length=2,min_length=1)
#
#
#     class Meta:
#         model = BookInfo
#         # fields是得到那些字段,__all__是全部字段包括hbook
#         # fields = '__all__'
#         fields =('id','hname','hbook','hcomment','hgender')
#         # 指明哪些字段只用序列化输出
#         # read_only_fields = ('id','hname')
#         # exclude是排除哪些字段
#         # exclude = ('id',)
#         # 添加额外参数
#         extra_kwargs = {
#             'hcomment':{'max_length':8,'required':False},
#             'hname':{'max_length':3,'min_length':2,'required':False}
#         }
