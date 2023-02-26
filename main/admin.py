from django.contrib import admin
from .models import Stech,Otzyv,Client

 

class OtzyvAdmin(admin.ModelAdmin):
    list_display =('id','name','text','tel','date')
    list_display_links= ('id','name','text','tel','date')
    search_fields=('id','name','text','tel','date',)


class StechAdmin(admin.ModelAdmin):
    list_display =('title', 'mod', 'photo', 'category', 'specs', 'prise', 'is_home')
    list_display_links= ('title', 'mod', 'photo', 'category', 'specs', 'prise', 'is_home')
    search_fields = ('title', 'mod', 'photo', 'category', 'specs', 'prise', 'is_home')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'call')
    list_display_links = ('name', 'tel', 'call')
    search_fields = ('name', 'tel', 'call')

admin.site.register(Stech,StechAdmin)
admin.site.register(Otzyv,OtzyvAdmin)
admin.site.register(Client,ClientAdmin)









    