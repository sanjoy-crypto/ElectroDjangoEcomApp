from django.contrib import admin
from .models import *

# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company','status','update_at']

admin.site.register(Setting,SettingAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status','note','create_at']
    readonly_fields = ['name','email','subject','message']
    list_filter = ['status']

admin.site.register(ContactMessage,ContactMessageAdmin)

admin.site.register(Slider)