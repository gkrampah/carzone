from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.car_photo.url))
    thumbnail.short_description = 'Car Image' #label for a column
    list_display = ('id','thumbnail','car_title', 'color', 'year', 'model', 'created_date', 'fuel_type', 'city', 'is_featured',)
    list_display_links = ('id', 'thumbnail', 'car_title',) #make it lickable
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'model', 'id', 'city') #what to  include in search 
    list_filter = ('city', 'fuel_type', 'body_style',) #set filter
admin.site.register(Car, CarAdmin)