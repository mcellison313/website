from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("birthday", views.birthday, name="birthday"),
    path("gallery", views.gallery, name="gallery")
]

