from django.db import models
import datetime as dt

# Create your models here.



class Location(models.Model):
    name = models.CharField(max_length=60)

    def save_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


    def save_category(self):
        self.save()


class Image(models.Model):
    name = models.CharField(max_length=60)
    imager = models.ImageField(upload_to="image/")
    description = models.TextField()
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)

    @classmethod
    def index(cls):
        today = dt.date.today()
        yo = cls.objects.filter(pub_date__date=today)
        return yo

    @classmethod
    def search_by_imager(cls, search_term):
        yo = cls.objects.filter(name__icontains=search_term)
        return yo

    @classmethod
    def display_images(cls):
        return cls.objects.all()
        
    @classmethod
    def search_by_category(cls,category):
        yo = Category.objects.filter(name__icontains = category)[0]
        return cls.objects.filter(category = yo.id)



    # @classmethod
    # def copy_image(image_url):
    #     find_image = Image.get_image_by_id(imager)
    #     return pyperclip.copy(find_image.imager)

    # @classmethod
    # def filter_by_location(cls,location):
    #    """
    #    This is the method to get images taken in a certain location
    #    """
    #    yo = Location.objects.get(name = location)
    #    return cls.objects.filter(location_id = yo.id)