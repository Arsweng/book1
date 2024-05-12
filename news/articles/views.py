from turtle import title
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

from .models import Article

# Create your views here.


class ArticlesListView(ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    login_url = 'login'

class ArticleDetailsView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'articles/article_details.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ('title','body')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles_list')
    login_url = 'login'

    def dispatch(self,request,*args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ('title','body',)
    login_url = 'login'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)



