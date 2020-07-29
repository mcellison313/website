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
    replies = Reply.objects.filter(post=postToShow)
    return render(request, "blog/post.html", {
        "post": postToShow,
        "replies": replies,

    })


def createPost(request):
    return None


def reply(request, post_id):
    if request.method == "POST":
        postToShow = Post.objects.get(pk=post_id)
        replies = Reply.objects.filter(post=postToShow)

        message = request.POST["replyText"]
        reply = Reply.objects.create()
        reply.message = message
        reply.author = request.user
        reply.post = postToShow
        print("made it here")
        reply.save()

        return render(request, "blog/post.html", {
            "post": postToShow,
            "replies": replies,

        })
