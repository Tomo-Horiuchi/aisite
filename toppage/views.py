"""
toppageのviwe
"""
from django.shortcuts import render

# Create your views here.
def topfunc(request):
    """
    トップページに遷移
    """

    return render(request, 'toppage/toppage.html')
