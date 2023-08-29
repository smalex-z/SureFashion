from django.shortcuts import render, redirect
from .models import Product, SimilarItem, Style
from .forms import ProductForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

#Homepage. Not much to see here
def home(request):
    return render(request, 'home/home.html')    


#Authentication Code- Login/Signup
def authentication_view(request):
    login_form = AuthenticationForm()
    signup_form = RegisterForm()
    
    #Login Code
    if 'login-btn' in request.POST:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('../wardrobe')

    #Signup Code
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


#Logout. Pretty Self-explaiatory imo. Parden the spelling
def logout_view(request):
    logout(request)
    return redirect('home')


#Wardrobe
@login_required
def wardrobe(request):
    #User can only see their own products
    products = Product.objects.filter(user=request.user)

    #Product Count
    product_count = products.count()
    
    #Sort the Wardrobe in order- Default is Newest
    sort_by = request.GET.get('sort', 'newest')
    
    if  sort_by == 'newest':
        products = products.order_by('-date_added')
    elif sort_by == 'heat':
        products = products.order_by('-heat_index')

    #Adding a product to your wardrobe
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


#Inspiration
@login_required
def inspiration(request):
    #User can only see their own products
    products = Product.objects.filter(user=request.user)
    
    

    context = {'products': products}

    return render(request, 'home/inspiration.html', context)


# Views for the admin-only page
@user_passes_test(lambda user: user.is_superuser)
def admin_items(request):
    products = SimilarItem.objects.filter()
    context = {'products': products}
    return render(request, 'home/wardrobe.html', context)

@user_passes_test(lambda user: user.is_superuser)
def admin_styles(request):
    products = Style.objects.filter()
    context = {'products': products}
    return render(request, 'home/wardrobe.html', context)
