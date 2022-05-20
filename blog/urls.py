from django.urls import path, include

from blog.views import PostListView


urlpatterns = [
    path('list/', PostListView.as_view(), name="post_list"),
]
