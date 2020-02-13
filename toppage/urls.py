"""ulls"""
from django.urls import path

from .views import topfunc
urlpatterns = [
    path('', topfunc, name='toppage'),
]
