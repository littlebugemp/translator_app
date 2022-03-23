from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView): #if need to render model data
    model = Post
    template_name = 'blog.html'

class HomeView(generic.TemplateView): #only render to template without model
    template_name = 'index.html'
