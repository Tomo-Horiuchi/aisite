from django.shortcuts import render
from django.contrib.auth.models import User

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
