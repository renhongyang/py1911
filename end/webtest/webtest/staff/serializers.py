from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name',read_only=True)

    class Meta:
        model = Employee
        fields = ('id','name','salary','department')

class DepartmentSerizlizer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)

    def create(self, validated_data):

        instance = Department.objects.create(**validated_data)

        return instance

    def update(self, instance, validated_data):

        instance.name = validated_data.get("name",instance.name)
        instance.save()
        return instance

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=5)
    department = DepartmentSerizlizer(label="部门")


    def validate_department(self,department):

        try:
            Department.objects.get(name = department["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")

        return department

    def validate(self, attrs):
        print("收到的数据为",attrs)
        try:
            d = Department.objects.get(name=attrs["department"]["name"])
        except:
            d = Department.objects.create(name = attrs["department"]["name"])
        attrs["category"] = d
        print("更改之后的数据",attrs)

        return attrs

    def create(self, validated_data):
        print("创建good参数",validated_data)
        instance = Employee.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.department = validated_data.get("department",instance.department)
        instance.save()
        return instance

class DepartmentSerizlizer(serializers.ModelSerializer):

    employees = serializers.SlugRelatedField(slug_field='name',many=True,read_only=True)
    class Meta:
        model = Department
        fields = ('id','name','employees')






