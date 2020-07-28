from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, "blog/index.html") #look at all of the blog posts