from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog, name="blog"),  # overall blog page
    path("<int:post_id>", views.post, name="post"),  # view individual post/reply


]
