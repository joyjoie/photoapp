from django.contrib import admin

# Register your models here.
from .models import Editor,Image,category,Location

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(category)
admin.site.register(Location)