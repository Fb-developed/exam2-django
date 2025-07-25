from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def register_view(request):
    if request.method == "GET":
        return render(request, 'autho/register.html')
    elif request.method == "POST":
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        confirm_password = request.POST.get('confirm_password', False)
        if not username or not email or not password or not confirm_password:
            return HttpResponse('Pleas fill all inputs')
        if not password == confirm_password:
            return render(request, 'authoo/register.html')
        user = User.objects.filter(username=username).exists()
        if user:
            return HttpResponse("error")
        new_user = User.objects.create_user(
            username=username,
            email=email
        )
        new_user.set_password(password)
        new_user.save()
        return redirect('login')
    

def login_view(request):
    if request.method == "GET":
        return render(request, "autho/login.html")
    elif request.method=="POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if not username  or not password:
            return render(request, 'autho/login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("income-list")
        return HttpResponse("eror")
    

def logout_view(request):
    try:
        logout(request)
        return redirect("login")
    except Exception as ex:
        return HttpResponse(str(ex))    


