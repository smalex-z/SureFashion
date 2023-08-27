from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home/home.html')    

def authentication_view(request):
    login_form = AuthenticationForm()
    signup_form = RegisterForm()
            
    if 'login-btn' in request.POST:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('../wardrobe')

    elif 'signup-btn' in request.POST:
        signup_form = RegisterForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('home')  # or where you want to redirect after a successful registration #TODO: Change this to Signup Success

    return render(request, 'home/authentication.html', {
        'login_form': login_form,
        'signup_form': signup_form
    })


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def wardrobe(request):
    products = Product.objects.filter(user=request.user)
    sort_by = request.GET.get('sort', 'price-asc')

    product_count = products.count()

    if sort_by == 'price-asc':
        products = products.order_by('price')
    elif sort_by == 'price-desc':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-date_added')


    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Set the current user as the owner of the product
            product.save()
            return redirect('../wardrobe')  # Redirect to the product listing page after successful creation
    else:
        form = ProductForm()

    context = {'products': products, 'product_count': product_count, 'form': form}

    return render(request, 'home/wardrobe.html', context)