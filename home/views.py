from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    return render(request, 'home/home.html')    

def wardrobe(request):
    products = Product.objects.all()
    sort_by = request.GET.get('sort')

    if sort_by == 'price-asc':
        products = products.order_by('price')
    elif sort_by == 'price-desc':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-date_added')

    context = {'products': products}

    return render(request, 'home/wardrobe.html', context)

