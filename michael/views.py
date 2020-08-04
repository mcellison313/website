import os
from website import settings

from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    return render(request, 'michael/index.html')


def birthday(request):
    today = datetime.datetime.now()
    return render(request, "michael/birthday.html", {
        "birthday": (today.day == 22) & (today.month == 7)
    })


def gallery(request):
    return render(request, 'michael/gallery.html', {

    })