from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('addtoshopcart/<int:id>/',addToShopCart,name="addtoshopcart"),
    path('deletefromcart/<int:id>/',deleteFromShopCart,name="deletefromcart"),
    path('orderproduct/',orderProduct,name="orderproduct"),
]