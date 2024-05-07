from django.urls import path
from .views import *
urlpatterns = [
    path('', BlogListView.as_view(),name = 'home'),
    path('post/<int:pk>',BLogDetailsView.as_view(),name='post_details')

]
