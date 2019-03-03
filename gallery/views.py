from django.shortcuts import render, redirect

from django.http  import HttpResponse

import datetime as dt
# from .models import Image,Location, Editor,category
# Create your views here.
def welcome(request):
   return render(request, 'welcome.html')


def index(request):
    date = dt.date.today()   
  
    return render(request, 'photos/index.html', {"date": date,})



def image(request, image):
    
    try:
        foto = Image.objects.get(id = image_id)

    except DoesNotExist:
        raise Http404()
    return render(request,"photos/image.html", {"foto":foto})




def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_imager(search_term)
        message = f"{search_term}"
        print(searched_images)

        return render(request, 'photos/search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any photo"
        return render(request, 'photos/search.html',{"message":message})    



def display_img(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        view_images = Image.image_upload(search_term)
        message = f"{search_term}"
        print(searched_images)

        return render(request, 'photos/image.html',{"message":message,"image": view_images})

    else:
        message = "You haven't gotten any photo"
        return render(request, 'photos/image.html',{"message":message})    
