from django.shortcuts import render 
from .models import Post 
def post(request):
    posts =Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})
