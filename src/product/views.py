from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import *

# Create your views here.
def product(request):
    return HttpResponse('<h1> Product Page </h1>')

def category_product(request,id,slug):
    products = Product.objects.filter(category_id=id)
    random_product = Product.objects.all().order_by('?')[:3]
    context = {'products':products,'random_product':random_product}
    return render(request,'categoryProduct.html',context)
    
def addComment(request,id):
    url = request.META.get('HTTP_REFERER')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.user_id = request.user.id
            data.product_id = id
            data.save()
            messages.success(request, 'Your review has been sent. Thank you for your review.')
            return redirect(url)
    return redirect(url)