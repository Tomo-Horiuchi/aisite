"""ulls"""
from django.urls import path

from .views import SatomiTop

urlpatterns = [
    path('', SatomiTop.as_view(), name='satomitop'),
]
