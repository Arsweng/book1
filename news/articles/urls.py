from django.urls import path
from .views import *

urlpatterns = [
path('<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_edit'), # new
path('<int:pk>/',ArticleDetailsView.as_view(), name='article_details'), # new
path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'), # new
path('', ArticlesListView.as_view(), name='articles_list'),
path('new/', ArticleCreateView.as_view(), name='article_new'),
]

