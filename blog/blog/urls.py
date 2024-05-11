from django.urls import path
from .views import *
urlpatterns = [
    path('', BlogListView.as_view(),name = 'home'),
    path('post/<int:pk>',BLogDetailsView.as_view(),name='post_details'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/edit/<int:pk>/',BlogUpdateView.as_view(),name='post_edit'),
    path('post/delete/<int:pk>/',BlogDeleteView.as_view(),name='post_delete'),
]
