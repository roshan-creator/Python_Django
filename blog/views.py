from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

def home(request):
    dess = Post.objects.all()    
    return render(request,'blog/home.html',{'dess':dess})

def insertdata(request):
    if request.method=="POST":
        Description=request.POST['description']
        Image=request.FILES['image1']
        Assign=request.POST['exampleFormControlSelect1']
            
        ins= Post(Description=Description,Image=Image,Assign=Assign)
        ins.save()


    return render(request,'blog/insert.html')