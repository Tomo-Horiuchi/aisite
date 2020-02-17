"""
satomiviwe
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PhotoForm
from .main import test
#from satomipage.main import pred

class SatomiTop(TemplateView):
    """
    画像受信処理
    """
    def __init__(self):
        self.params = {'msg': 'idx', 'form': PhotoForm(),}

    def get(self, req):
        """
        get処理
        """
        msg = '画像を選択してください'
        self.params['msg'] = msg
        return render(req, 'satomipage/satomitop.html', self.params)

    def post(self, req):
        """
        post処理
        """
        form = PhotoForm(req.POST, req.FILES)
        form.save()
        if not form.is_valid():
            raise ValueError('invalid form')

        #self.params['pred'] = pred(image)
        return render(req, 'satomipage/satomitop.html', self.params)
