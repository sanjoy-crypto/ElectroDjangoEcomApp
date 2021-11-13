from django.urls import path
from .views import * 


urlpatterns = [
    path('',userProfile,name='user'),
    path('user_update',userUpdate,name='user_update'),
    path('password/',userPassword,name='user_password'),
    path('orders/',userOrders,name='user_orders'),
    path('orderdetail/<int:id>/',userOrdersDetails,name='user_orders_details'),
    path('orders_product',userOrdersProducts,name='user_orders_product'),
    path('comments/',userComments,name='user_comments'),
    path('deletecomment/<int:id>/',userCommentsdelete,name='deletecomment'),
]