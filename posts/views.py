from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
import random
from posts.forms import PostForm, PostForm2



def test_view(request):
    return HttpResponse(random.randint(1, 100))


def main_page_view(request):
    return render(request,  'base.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", context={"posts": posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post_detail.html", context={"post": post})

def post_create_view(request):
    if request.method == "GET":
        # form = PostForm
        form = PostForm2
        return render(request, "post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "post_create.html", context={"form": form})
        form.save()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # image = form.cleaned_data.get("image")
        # post = Post.objects.create(title=title, content=content, image=image)
        return redirect("/posts/")
