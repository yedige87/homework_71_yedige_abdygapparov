from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import ArticleSerializer, CommentsSerializer
from webapp.models import Article


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_superuser


class ArticleSimpleView(View):

    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        serializer = ArticleSerializer(objects, many=True)
        return JsonResponse(serializer.data)


class ArticleView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_example(self, request, *ars, **kwargs):
        return JsonResponse({'message': 'HelloWorld'})

    def get_comments(self, request, *ars, **kwargs):
        article = self.get_object()
        serializer = CommentsSerializer(article.comments.all(), many=True)
        return Response(serializer.data)