from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db import models
# Create your views here.
from blog.models import Post, Reply
from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea())



class ReplyForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea())


def index(request):
    return render(request, "blog/index.html", {
        "posts": Post.objects.all(),
        "form": PostForm
    })


def post(request, post_id):
    # current post:
    post = Post.objects.get(pk=post_id)
    # current replies
    allReplies = Reply.objects.filter(post=post)

    if request.method == "POST":
        if not (request.user.is_authenticated()):
            return render(request, "blog/post.html", {
                "post": post,
                "replies": allReplies,
                "form": ReplyForm,
                "message": "Please Log In to Post Reply"
            })
        form = ReplyForm(request.POST)

        if form.is_valid():  # create new reply and save DOES NOT CHECK FOR VALID USER
            message = form.cleaned_data["message"]
            user = request.user

            reply = Reply.objects.create(message=message, author=user, post=post)
            reply.save()
            #after saving replies, update list to show
            allReplies = Reply.objects.filter(post=post)

            # return render of blog post with new replies
            return render(request, "blog/post.html", {
                "post": post,
                "replies": allReplies,
                "form": ReplyForm
            })

        else:  # form not valid
            return render(request, "blog/post.html", {
                "post": post,
                "replies": allReplies,
                "message": 'Form Not Valid',
                "form": ReplyForm
            })

    # return if not POST or not logged in
    return render(request, "blog/post.html", {
        "post": post,
        "replies": allReplies,
        "form": ReplyForm
    })









