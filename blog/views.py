from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.
from blog.models import Post, Reply


def index(request):
    return render(request, "blog/index.html", {
        "posts": Post.objects.all()
    })


def post(request, post_id):
    postToShow = Post.objects.get(pk=post_id)
    replies = Reply.objects.filter(post = postToShow)
    return render(request, "blog/post.html", {
        "post": postToShow,
        "replies": replies,

    })