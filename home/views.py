from django.shortcuts import render, redirect
from .models import Product, SimilarItem, Style, UserProfile
from .forms import ProductForm, RegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
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
    profile_form = UserProfileForm()
    
    #Login Code
    if 'login-btn' in request.POST:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('../wardrobe')

    # Signup Code
    elif 'signup-btn' in request.POST:
        signup_form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')

    return render(request, 'home/authentication.html', {
        'login_form': login_form,
        'signup_form': signup_form,
        'profile_form': profile_form  # Add this line
    })

@login_required
def user_profile(request):
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user)

    if request.method == "POST":
        # Handle the form submission
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #TODO: Django Messages/Alerts? - messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'home/profile.html', context)

#Logout. Pretty Self-explaiatory imo. Parden the spelling
def logout_view(request):
    logout(request)
    return redirect('home')


#Wardrobe
@login_required
def wardrobe(request):
    #User can only see their own products
    products = Product.objects.filter(user=request.user)
    styles = Style.objects.filter()
    SimilarItems = SimilarItem.objects.filter()

    #Product Count
    product_count = products.count()
    
    #Sort the Wardrobe in order- Default is Newest
    sort_by = request.GET.get('sort', 'newest')
    
    if  sort_by == 'newest':
        products = products.order_by('-date_added')
    elif sort_by == 'heat':
        products = products.order_by('heat_index')
    elif sort_by == 'formality':
        products = products.order_by('formality')


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

    context = {'products': products, 'product_count': product_count, 
               'form': form, 'styles': styles, 'SimilarItems': SimilarItems}

    return render(request, 'home/wardrobe.html', context)


#Inspiration
@login_required
def inspiration(request):
    #User can only see their own products
    products = Product.objects.filter(user=request.user)
    #print(products[1])
    
    

    context = {'products': products}

    return render(request, 'home/inspiration.html', context)

def generate(request):
    products = Product.objects.filter(user=request.user)

    outerwear, tops, bottoms, shoes, accessories, errors = []

    #sort the products
    for product in products:
        #TODO: Surely theres a cleaner way of doing this
        #TODO: figure out how to do product.id but with category instead
        if product.id == 'outerwear':
            outerwear.append(product) 
        elif product.id == 'top':
            tops.append(product)
        elif product.id == 'bottom':
            bottoms.append(product)
        elif product.id == 'shoes':
            shoes.append(product)
        elif product.id == 'accessories':
            accessories.append(product)
        else:
            print("How'd we end up here? Category Error")
            errors.append(product)


    

    
    return 






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
