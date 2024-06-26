from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','age','is_author',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields = ('username', 'email', 'age','is_author')


        