from django.http import JsonResponse
from rest_framework import serializers
from webapp.models.articles import StatusChoice, Article


class CommentsSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000, min_length=5, required=True, allow_blank=True)
    author = serializers.CharField(max_length=200, required=True, allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class ArticleSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(default=0, read_only=True, source='comments.count')
    comments_count_v2 = serializers.SerializerMethodField(default=0, read_only=True, source='comment_count_v2')
    title = serializers.SerializerMethodField(read_only=True, source='get_title')

    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'author', 'created_at', 'updated_at', 'comments_count', 'comments_count_v2')
        read_only_fields = ('id', 'created_at', 'updated_at', 'comments')

    def get_comment_count(self, obj: Article):
        return obj.comments.count()

    def get_title(self, obj: Article):
        return obj.title.upper()









# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200, required=True, allow_blank=True)
#     text = serializers.CharField(max_length=1000, min_length=5, required=True, allow_blank=True)
#     author = serializers.CharField(max_length=200, required=True, allow_blank=True)
#     status = serializers.ChoiceField(choices=StatusChoice, required=False, default=StatusChoice.ACTIVE)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     comments = CommentsSerializer(many=True, read_only=True)

    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)
    #
    # def update(self, instance: Article, validated_data):
    #     for field, value in validated_data.items():
    #         setattr(instance, field, value)
    #     instance.save()


