from django.shortcuts import render, redirect

from django.http  import HttpResponse

# import datetime as dt
from .models import Image,Location,Category
# Create your views here.

# def welcome(request):
#     images = Image.display_images()
#     return render(request, 'welcome.html',{"images":images})


def index(request):
    images = Image.display_images() 
  
    return render(request, 'photos/index.html',{"images":images} )



def image(request, image):
    
    try:
        foto = Image.objects.get(id = image_id)

    except DoesNotExist:
        raise Http404()
    return render(request,"photos/image.html", {"foto":foto})




def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
       

        return render(request, 'photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any photo"
        return render(request, 'photos/search.html',{"message":message})    



def display_img(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        view_images = Image.image_upload(search_term)
        message = f"{search_term}"
        print(searched_images)

        return render(request, 'photos/image.html',{"message":message,"images": view_images})

    else:
        message = "You haven't gotten any photo"
        return render(request, 'photos/image.html',{"message":message})    



def location(request,location):
        locations = Image.filter_by_location(location)
        return render(request,'location.html',{"images": locations})
    