from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db import models
# Create your views here.
from blog.models import Post, Reply


def index(request):
    return render(request, "blog/index.html", {
        "posts": Post.objects.all()
    })


def post(request, post_id):
    postToShow = Post.objects.get(pk=post_id)
    replies = Reply.objects.filter(post=postToShow)
    return render(request, "blog/post.html", {
        "post": postToShow,
        "replies": replies,

    })


def createPost(request):
    return None

# litterally cant get anything to work
# shit is really pissing me off
def reply(request, post_id):
    return render(request, "", {

    })
    postToShow = Post.objects.get(pk=post_id)
    replies = Reply.objects.filter(post=postToShow)
    if request.method == "POST":
        temp = "help me"


        message = request.POST["replyText"]
        reply = Reply.objects.create()

        reply.message = models.TextField(message)
        reply.author = request.user
        reply.post = postToShow
        print("made it here")
        reply.save()

        return render(request, "blog/post.html", {
            "post": postToShow,
            "replies": replies,
            "message": temp
        })
