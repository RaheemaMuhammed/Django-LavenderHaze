from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,UserProfile
from django.utils.html import format_html
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))

    thumbnail.short_description ='Profile Picture'
    list_display    =   ('thumbnail','user','city','state','country')

class AccountAdmin(UserAdmin):
    list_display=('email','name','last_login','date_joined','is_active')
    list_display_links=('email','name','date_joined')
    readonly_fields=('last_login',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    ordering = ('date_joined', )

admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)