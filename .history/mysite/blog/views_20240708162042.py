from django.shortcuts import render 
from .models import Post 
def post(request):
    post =Post.objects.all()
    return render(request,'blog/post_list.html')