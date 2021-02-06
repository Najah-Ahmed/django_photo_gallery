from django.urls import path
from .views import addPhoto,showPhoto,detailsPhoto


urlpatterns =[
  path('',showPhoto,name="gallery"),
  path('photo/<str:pk>',detailsPhoto,name="details"),
  path('add',addPhoto,name="add"),

]