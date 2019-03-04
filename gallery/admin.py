from django.contrib import admin

# Register your models here.
from .models import Editor,Image,Category,Location

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('Category',)

admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)