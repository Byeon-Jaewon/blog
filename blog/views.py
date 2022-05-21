from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post

# Create your views here.
class PostListView(ListView):
    template_name="blog/list.html"
    queryset = Post.objects.all()
    context_object_name = "post_list"


class PostDetailView(DetailView):
    template_name="blog/detail.html"
    model = Post
    context_object_name = "post"