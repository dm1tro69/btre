from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pablished', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('is_pablished',)
    search_fields = ('title', 'description', 'addres', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25


# Register your models here.
admin.site.register(Listing, ListingAdmin)
