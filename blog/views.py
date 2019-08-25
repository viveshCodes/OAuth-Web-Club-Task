from django.shortcuts import render
from . models import Look
from django.contrib.auth.decorators import login_required
def blog_home(request):
    return render(request,'blog/blog.html')

@login_required(login_url="/account/signin")
def blog_look(request):
    looks= Look.objects.all().order_by('date')
    return render(request,'blog/bloglook.html',{"looks":looks})