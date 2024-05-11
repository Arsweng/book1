
from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'all_posts_list'

class BLogDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("home")

# Create your views here.
