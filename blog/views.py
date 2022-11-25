from django.shortcuts import render
from django.views import generic

from .models import Post

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts.html'


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'
