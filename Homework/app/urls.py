from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from api.views import PostAPIView, PostAPIDeleteView, \
    PostAPICreateView, PostAPIUpdateView, PostAPIDetailView
from posts.views import HomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path('api/posts/', PostAPIView.as_view()),
    path('api/posts/<int:pk>', PostAPIDetailView.as_view()),
    path('api/posts/update/<int:pk>', PostAPIUpdateView.as_view()),
    path('api/posts/create', PostAPICreateView.as_view()),
    path('api/posts/delete/<int:pk>', PostAPIDeleteView.as_view()),
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path("posts/", include("posts.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

