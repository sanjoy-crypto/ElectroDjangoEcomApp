from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from home.forms import SearchForm
from home.models import *
from product.models import *
import json
# Create your views here.
def index(request):
    sliders = Slider.objects.all().order_by('-id')[:4]
    page = "home"
    latest_product = Product.objects.all().order_by('-id')[:8]
    random_product = Product.objects.all().order_by('?')[:8]
    context = {'page':page,'sliders':sliders,'latest_product':latest_product,'random_product':random_product}
    return render(request,'index.html',context)

def AboutPage(request):
    context = {}
    return render(request,'about.html',context)

def ContactPage(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']


            form.save()
            messages.success(request, 'Your message has been sent. Thank you for your message.')
            return redirect('contact_us')

    context = {'form':form}
    return render(request,'contact.html',context)


def search(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query,category_id = catid)
            
            context = {'products':products,'query':query}
            return render(request,'searchProduct.html',context)

    return redirect('/')

def searchAuto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title 
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

# Product Details 

def product_details(request,id,slug):
    product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('?')[:8]
    comments = Comment.objects.filter(product_id=id,status="True").order_by('-id')

    # review = Comment.objects.filter(product_id=id,status="True").aggregate(Count('id').Avg('rate'))
    
    context = {'product':product,'images':images,'products':products,'comments':comments}
    return render(request,'productDetails.html',context)



def Faq(request):
    faq = FAQ.objects.filter(status="True").order_by("ordernumber")

    return render(request,'faq.html',{'faq':faq})
