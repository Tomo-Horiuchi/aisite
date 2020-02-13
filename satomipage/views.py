"""
satomiviwe
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PhotoForm
#from satomipage.main import pred

class SatomiTop(TemplateView):
    def __init__(self):
        self.params={'pred': 'idx', 'form': PhotoForm(), 'image':'img'}

    def get(self, req):
        return render(req, 'satomipage/satomitop.html', self.params)

    def post(self, req):
        form = PhotoForm(req.POST, req.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')
    
        image = form.cleaned_data['image']
        self.params['image'] = image
        #self.params['pred'] = pred(image)
        return render(req, 'satomipage/satomitop.html', self.params)