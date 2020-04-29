from rest_framework import serializers
from .models import *

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.title',read_only=True)

    class Meta:
        model = Goods
        fields = "__all__"

class CategorysSerizlizer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=10, min_length=2, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少2个字"
    })

    def create(self, validated_data):

        instance = Categorys.objects.create(**validated_data)
        # print("创建模型实例",instance)
        return instance

    def update(self, instance, validated_data):

        # print("重写更新方法",validated_data,instance.name)
        instance.name = validated_data.get("title", instance.name)
        # print(instance.name)
        instance.save()
        return instance

class IndexcategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indexcategorys
        fields = "__all__"

class IndexgoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indexgoods
        fields = "__all__"


class TimegoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timegoods
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(write_only=True)
    # password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        # __all__ 代表模型中的所有字段
        # fields = "__all__"
        # 不显示某些字段
        exclude = ["user_permissions", "groups", "first_name", "last_name", "password"]

    def validate(self, attrs):
        # 对用户密码进行哈希加密，在数据库中不会以明文显示
        from django.contrib.auth import hashers
        if attrs.get("password"):
            attrs["password"] = hashers.make_password(attrs["password"])
        return attrs

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10, min_length=3, error_messages={
        "required": "用户名必填！"
    })
    password = serializers.CharField(max_length=10, min_length=3, error_messages={
        "required": "需填写密码！"
    })
    password1 = serializers.CharField(max_length=10, min_length=3, write_only=True, error_messages={
        "required": "需再次填写相同密码！"
    })
    telephone = serializers.CharField(max_length=11, min_length=11, write_only=True, error_messages={
        "required": "需要输入11位手机号码！"
    })
    email = serializers.CharField(max_length=18, min_length=6, write_only=True, error_messages={
        "required": "需要输入邮箱号！"
    })

    # def validate_password1(self, data):
    #     if data != self.initial_data["password"]:
    #         raise serializers.ValidationError("两次密码不一致！")
    #     else:
    #         return data
    def validate(self, attrs):
        if attrs["password"] != attrs["password1"]:
            raise serializers.ValidationError("两次密码不一致！")
        else:
            del attrs["password1"]
            return attrs

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get("username"), email=validated_data.get("email"),
                                        password=validated_data.get("password"), telephone=validated_data.get("telephone"))

        # 通用创建,密码不被加密
        # return User.objects.create(**validated_data)

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = "__all__"
