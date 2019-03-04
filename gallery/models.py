from django.db import models
import datetime as dt

# Create your models here.


class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()


class Location(models.Model):
    name = models.CharField(max_length=60)

    def save_location(self):
        self.save()


class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=60)
    imager = models.ImageField(upload_to='image /')
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    category = models.ManyToManyField(category)
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
    def display_images(cls, display_img):
        imag = cls.object.filter(imager_icontains=display_img)
        return imag
