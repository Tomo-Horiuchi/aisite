"""
satomipageのform
"""
from django import forms
from .models import SatomiImg

class PhotoForm(forms.ModelForm):
    """
    画像アップロード用
    """
    class Meta:
        model = SatomiImg
        fields = ('image',)
