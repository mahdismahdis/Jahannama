from django.shortcuts import render, get_object_or_404,redirect
from . models import Category,Product,Gallery
from django.utils.translation import gettext_lazy as _


# Create your views here.

def index(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_list = product_list.filter(title__icontains=item_name)

    return render(request, 'myapp/index.html',
                  {'category_list': category_list, 'product_list': product_list, 'item_name': item_name})

def category_product(request,pk):
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category)
    context = {'products':products, 'category':category}

    return render(request, 'myapp/category_product.html', context)

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

# def gallery(request):
#     return render(request, 'myapp/gallery.html')


def gallery(request):
    images = Gallery.objects.all()

    return render(request, "myapp/gallery.html", {
        "images": images,
    })