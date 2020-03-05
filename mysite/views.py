from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Posts
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("Not working")
        

    else:
        form = PostForm()
        context = {'form':form}
        return render(request,'main.html',context)

def files(request):
    posts = Posts.objects.all()
    context = {'posts':posts}
    return render(request,'photo.html',context)