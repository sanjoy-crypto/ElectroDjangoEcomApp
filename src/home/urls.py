from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='home'),
    path('about/',AboutPage,name="about_us"),
    path('contact/',ContactPage,name="contact_us"),
    path('search/',search,name="search"),
    path('faq/',Faq,name='faq'),
    path('search_auto/',searchAuto,name="search_auto"),
     path('product/<int:id>/<slug:slug>/',product_details,name='product_details'),
]