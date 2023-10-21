from rest_framework import serializers
from .models import Report
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
			'title',
			'author',
			'description',
			'category',
			'file_path',
			'create_time'
		]


	def get_create_time(self, obj):
		return obj.create_at
