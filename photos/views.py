from django.shortcuts import render

def showPhoto(request):
    return render( request,'photos/gallery.html')


def addPhoto(request):
    return render( request,'photos/add.html')

def detailsPhoto(request,pk):
      return render( request,'photos/details.html')