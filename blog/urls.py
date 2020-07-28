from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  #overall blog page
    #path("<int:post_id>", views.blog, name="post"),  #view individual post

]