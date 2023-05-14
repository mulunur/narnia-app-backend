from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.createImage, name="create"),
    path("<int:image_id>/", views.getImage, name="getImage"),
    path("getAll/", views.getAllImages, name="getAllImages")
]