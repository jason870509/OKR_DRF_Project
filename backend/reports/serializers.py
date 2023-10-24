from rest_framework import serializers
from .models import Report, Category
from user.serializers import UserPublicSerializer


class CategoryPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField(read_only=True)


class ReportSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(read_only=True)
    category = CategoryPublicSerializer(read_only=True)
    create_time = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Report
        fields = [
            'id',
            'title',
            'author',
            'description',
            'category',
            'file_path',
            'create_time'
        ]


    def get_create_time(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Report):
            return None
        return obj.create_at


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'category'
        ]
