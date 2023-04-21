from django.urls import path

from webapp.views.articles import ArticleDetail, ArticleUpdateView, \
    ArticleCreateView, ArticleDeleteView, FavoriteView
from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.example import echo, get_token_view, json_articles, json_article_delete

urlpatterns =[
    path("", IndexView.as_view(), name='index'),
    path("article/", IndexRedirectView.as_view(), name='articles_index_redirect'),
    path('article/add/', ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/confirm_delete/', ArticleDeleteView.as_view(), name='confirm_delete'),
    path('articles/<int:pk>/to-favorite', FavoriteView.as_view(), name='to_favorite'),
    path('echo/', echo, name='echo'),
    path('token/', get_token_view, name='token'),
    path('json-articles/', json_articles, name='json_articles'),
    path('json-articles/<int:pk>', json_article_delete, name='json_article_delete'),
]

