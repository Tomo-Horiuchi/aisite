"""
satomipageのform
"""
from django import forms

class PhotoForm(forms.Form):
    """
    画像アップロード用
    """
    image = forms.ImageField()