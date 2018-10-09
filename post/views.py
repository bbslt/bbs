from django.shortcuts import render, redirect

from post.models import Post

# Create your views here.

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        post = Post.objects.create(title=title,content=content)
        '''
        post = Post(title=title,content=content)
        post.save()
        '''
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        return render(request,'create_post.html',{})


def edit_post(request):
    return render(request,'edit_post.html',{})


def read_post(request):
    post_id = int(request.GET.get("post_id"))
    post = Post.objects.get(pk=post_id)
    return render(request,'read_post.html',{'post':post})


def delete_post(request):
    return render(request,'delete_post.html',{})


def post_list(request):
    return render(request,'post_list.html',{})


def seach(request):
    return render(request,'search.html',{})