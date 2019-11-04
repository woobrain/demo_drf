from django.http import JsonResponse
from rest_framework import serializers


# 自定义序列化器
from book.models import BookInfo


class BookSerializer(serializers.Serializer):
    # 定义序列化器字段  字段选项验证
    # read_only表示该字段只进行序列化返回
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField(max_length=20, min_length=4)
    bread = serializers.IntegerField(max_value=100, min_value=0)
    # 默认情况下required=True表示该字段必传  write_only 只参与反序列化
    bpub_date = serializers.DateField(write_only=True,required=False)
    bcomment = serializers.IntegerField(default=0)

    # 父表嵌套子表返回
    # 关联表的字段 PrimaryKeyRelatedField返回关联表的id数据
    # heros = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # StringRelatedField 返回关联表的str方法的值
    # heroinfo_set = serializers.StringRelatedField(read_only=True,many=True)
    # 根据另外一个序列器指定的字段
    # heros= HeroSerialzier(read_only=True, many=True)

    # 自定以方法验证字段
    # 单一字段验证
    def validate_id(self, value):

        if value['id'] is None:
            raise serializers.ValidationError('此书不存在')

        return value
    def validate_btitle(self, value):
        """

        :param value:  接受该字段value值
        :return:
        """
        if value == 'python':
            # 抛出的异常被视图中的error属性获取
            raise serializers.ValidationError('书名不能python')

        # if len(value['btitle']) >= 20 or len(value['btitle']) <= 4:
        #     raise serializers.ValidationError('书名长度不符合要求')
        # 注意！！ 一定要将验证后的结果返回
        return value

    # 多个字段验证
    def validate(self, attrs):
        """

        :param attrs: 接受前端传递验证数据 类型 字典
        :return:
        """
        if attrs['bread'] > attrs['bcomment']:
            raise serializers.ValidationError('阅读量大于了评论量')

        return attrs


    def create(self, validated_data):
        """
            保存数据库
        :param validated_data:  验证成功后的数据
        :return:
        """
        book = BookInfo.objects.create(**validated_data)

        # 将保存的后的数据对象返回给序列化进行序列化返回
        return book


    def update(self, instance, validated_data):

        res = BookInfo.objects.filter(id=instance.id).update(**validated_data)
        if res == 0:
            return JsonResponse({"error": "更新失败"})
        book = BookInfo.objects.get(id=instance.id)
        return book


class HeroSerialzier(serializers.Serializer):
    id = serializers.IntegerField()
    hname = serializers.CharField()
    hgender = serializers.IntegerField()
    hcomment = serializers.CharField()

    # 子表嵌套父表
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # hbook = serializers.StringRelatedField(read_only=True)
    hbook = BookSerializer()

# 关联查询
# 父表查询子表
# book.heros.all()
# 子表查询父表
# hero.hbook.btitle
# 关联过滤查询


# class UserSerialzier(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     username=serializers.CharField()
#     password=serializers.CharField(write_only=True)
