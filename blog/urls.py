from django.urls import path, include

from blog.views import PostListView, PostDetailView


urlpatterns = [
    path('list/', PostListView.as_view(), name="post_list"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),
]
