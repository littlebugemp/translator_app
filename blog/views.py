from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView): #if need to render model data
    model = Post
    template_name = 'blog.html'

class AboutView(generic.TemplateView): #only render to template without model
    template_name = 'about.html'

class PostList(generic.ListView): #rendering multiple data rows ex post
    queryset = Post.objects.filter(status=1).order_by('date_created')
    template_name = "index.html"