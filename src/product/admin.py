from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status','create_at','image_tag']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','price','old_price','amount','minamount','status','create_at','image_tag']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Product,ProductAdmin)