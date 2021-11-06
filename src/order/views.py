from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def index(request):
    return HttpResponse('<h1>Order Page</h1>')

def addToShopCart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    checkproduct = ShopCart.objects.filter(product_id=id)

    if checkproduct:
        control = 1
    else:
        control = 0

    # this is come from product details form 
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart ")
        return redirect(url)

    # this is come from Home and other page product 
    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, "Product added to Shopcart")
        return redirect(url)


def shopCart(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total_items = sum([item.quantity for item in shopcart])
    total = sum([item.product.price * item.quantity for item in shopcart])

    context = {'total': total,'shopcart': shopcart, 'total_items': total_items}
    return render(request, 'shopcart_products.html', context)

@login_required(login_url='/login')
def deleteFromShopCart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return redirect("/shopcart")