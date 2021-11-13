from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from user.forms import *
from order.models import *
from django.contrib.auth.forms import PasswordChangeForm

from user.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse('<h1>User Page</h1>')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url

            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.warning(request,"Login Error !! Username or Password is invalid")
            return redirect('login')

    context = {}
    return render(request,'login.html',context)


def signup_page(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image='user.png'
            data.save()
            messages.success(request,"Your account has been created")
            return redirect('/')
        else:
            messages.warning(request,form.errors)
            return redirect('/signup')
    context = {'form':form}
    return render(request,'signup.html',context)


def logout_page(request):
    logout(request)
    return redirect('login')


def userProfile(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {'profile':profile}
    return render(request,'user_profile.html',context)


@login_required(login_url='/login')
def userUpdate(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')
    else:

        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login')
def userPassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/user')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('/user/password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form})

@login_required(login_url='/login')
def userOrders(request):
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {'orders': orders}
    return render(request, 'user_orders.html', context)

@login_required(login_url='/login')
def userOrdersDetails(request,id):
    order = Order.objects.get(user_id=request.user.id,id=id)
    orderitems = order.orderproduct_set.all()
    context = {'order':order,'orderitems':orderitems}
    return render(request,'user_order_detail.html',context)


def userOrdersProducts(request):
    order_product = OrderProduct.objects.filter(user_id = request.user.id).order_by('-id')
    context = {'order_product':order_product}
    return render(request,'user_order_products.html',context)


def userComments(request):
    current_user = request.user
    comments = Comment.objects.filter(user_id = current_user.id)
    context = {'comments':comments}
    return render(request,'user_comments.html',context)


def userCommentsdelete(request,id):
    Comment.objects.get(user_id = request.user.id, id=id).delete()
    messages.success(request,'Your comment deleted successfully')
    return redirect('user_comments')

