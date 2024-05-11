from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',SignUpUserView.as_view(),name='signup_user')
]
