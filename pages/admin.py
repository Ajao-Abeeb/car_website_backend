from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAmin(admin.ModelAdmin):
    def thumbmail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%; " />'.format(object.photo.url) )
    thumbmail.short_description = 'photo'
    list_display = ('id','thumbmail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id','first_name',)
    search_fields =('first_name','thumbmail','last_name','designation')
    list_filter = ('designation',)
admin.site.register(Team , TeamAmin)
