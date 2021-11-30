from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.photo.url))
    thumbnail.short_description = 'photo' #label for a column
    list_display= ('id', 'thumbnail', 'first_name', 'designation', 'created_date') #what to dis[lay on admin page
    list_display_links = ('id', 'thumbnail', 'first_name',) #make it lickable
    search_fields = ('first_name', 'last_name', 'designation') #what to  include in search 
    list_filter = ('designation',) #set filter
admin.site.register(Team, TeamAdmin)
