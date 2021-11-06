from home.models import Setting
from product.models import Category
from order.models import ShopCart


def get_filters(request):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total_items = sum([item.quantity for item in shopcart])
    total = sum([item.product.price * item.quantity for item in shopcart])

    data = {
        'setting':setting,
        'category':category,
        'total_items':total_items,
        'total':total,
        'shopcart':shopcart,

    }
    return data