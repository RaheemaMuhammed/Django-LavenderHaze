from django.contrib import admin
from . models import Cart, CartItem
# Register your models here.

class cartAdmin(admin.ModelAdmin):
    list_display=('cart_id','date_added')

class cartItemAdmin(admin.ModelAdmin):
    list_display=('user','product','cart','quantity')

admin.site.register(CartItem,cartItemAdmin)
admin.site.register(Cart,cartAdmin)