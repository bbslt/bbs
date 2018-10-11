from math import ceil

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
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        post = Post.objects.get(pk=post_id)
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect('post/read/?post_id=%d' % post.id)
    else:
        post_id = int(request.GET.get("post_id"))
        post = Post.objects.get(pk=post_id)
        return render(request,'edit_post.html',{"post":post})


def read_post(request):
    post_id = int(request.GET.get("post_id"))
    post = Post.objects.get(pk=post_id)
    return render(request,'read_post.html',{'post':post})


def delete_post(request):
    post_id = int(request.GET.get("post_id"))
    post = Post.objects.get(pk=post_id).delete()
    return redirect("/")


def post_list(request):
    #当前页数
    page = int(request.GET.get("page",1))
    #文章总数
    total = Post.objects.count()
    #每页文章数
    per_page = 10
    #总页数
    pages = ceil(total/per_page)
    start = (page - 1) * per_page
    end = start + per_page
    posts = Post.objects.all()[start:end]
    # posts = Post.objects.all().order_by("-id")
    return render(request,'post_list.html',{"posts":posts,"pages":range(pages)})


def search(request):
    keyword = request.POST.get("keyword")
    posts = Post.objects.filter(content__contains=keyword)
    return render(request,'search.html',{'posts':posts})