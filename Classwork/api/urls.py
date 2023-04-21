from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import ArticleView

router = routers.DefaultRouter()
router.register('articles', ArticleView)

urlpatterns =[
    path("", include(router.urls)),
    path("example/", ArticleView.as_view({'get': 'get_example'}), name='example'),
    path("articles/<int:pk>/comments", ArticleView.as_view({'get': 'get_comments'}), name='comments'),
    path('login/', obtain_auth_token, name='obtain_auth_token')
]
