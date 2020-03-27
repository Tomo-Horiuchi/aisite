from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

def signupfunc(request):
    if request. method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'bordapp/signup.html', {'error':'すでに登録されているユーザーです'})
        except:
            user = User.objects.create_user(username, '', password)
            return render(request, 'bordapp/signup.html', {'some': 100})
        print(request.POST)
    return render(request, 'bordapp/signup.html', {'some': 100})

def loginfunc(request):
    if request. method== 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'bordapp/login.html', {'some': 100})

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'bordapp/list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object_detail = BoardModel.objects.get(pk=pk)
    return render(request, 'bordapp/detail.html', {'object_detail':object_detail})

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')

class BoardCreate(CreateView):
    template_name = 'bordapp/create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')