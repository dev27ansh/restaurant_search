from django.contrib import admin
from .models import Restaurant, Item 




class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['name', 'location', 'id','lat_long']  

admin.site.register(Restaurant, RestaurantAdmin)


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name', 'price', 'restaurant__name']

admin.site.register(Item, ItemAdmin)