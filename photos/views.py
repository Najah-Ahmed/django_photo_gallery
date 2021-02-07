from django.shortcuts import render
from .models import Category, Photo

def showPhoto(request):
 
  categories=Category.objects.all()
  photos=Photo.objects.all()
  context={'categories':categories,'photos':photos}
  return render( request,'photos/gallery.html',context)


def addPhoto(request):
  return render( request,'photos/add.html')

def detailsPhoto(request,pk):
  photo=Photo.objects.get(id=pk)
  context={'photo':photo}
  return render( request,'photos/details.html',context)