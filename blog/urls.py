from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'blog'
urlpatterns = [
    #path('', TemplateView.as_view(template_name='blog/index.html'), name='index'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/<str:slug>', views.PostDetailView.as_view(), name='post'),
]
