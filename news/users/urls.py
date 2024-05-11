from django.urls import path
from .views import SignUpUserView

urlpatterns = [
    path('signup/',SignUpUserView.as_view(),name='signup')
]
