from django.contrib import admin
from .models import *

# Register your models here.


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    list_per_page = 50 



class WheelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')
    list_display_links = ('id', 'name')
    list_per_page = 50 



class EndorsementAdmin(admin.ModelAdmin):
    list_display = ('id', 'business')
    list_display_links = ('id', 'business')
    list_per_page = 50 


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'business')
    list_display_links = ('id', 'title')
    list_per_page = 50 



class ShelfAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')
    list_display_links = ('id', 'name')
    list_per_page = 50 


class ShelfPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_published', 'is_ad')
    list_display_links = ('id', 'name')
    list_per_page = 50 
    list_editable = ('is_published', 'is_ad')



admin.site.register(Business, BusinessAdmin)
admin.site.register(Wheel, WheelAdmin)
admin.site.register(Endorsement, EndorsementAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(ShelfPhoto, ShelfPhotoAdmin)

