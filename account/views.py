from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect
    else:
        form=AuthenticationForm()
    return render(request,"index.html",{"form":form})


def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)


    else:
        form=UserCreationForm()
    return render(request,"account/signup.html",{"form":form})



def signout(request):
    if request.method=='POST':
        logout(request)
        return render(request,'index.html')
