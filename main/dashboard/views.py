from django.shortcuts import render, redirect
from main import models

def index(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

# ---------CATEGORY-------------

def category_list(request):
    queryset = models.Category.objects.all()
    context = {'queryset': queryset}
    return render(request, 'dashboard/category/list.html', context)


def category_create(request):
    if request.method == 'POST':
        models.Category.objects.create(name=request.POST['name'])
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/category/create.html')


def category_update(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
    return redirect('dashboard:category_list')


def category_delete(request, id):
    category = models.Category.objects.get(id=id)
    category.delete()
    return redirect('dashboard:category_list')

# ---------PRODUCT-------------

def product_list(request):
    queryset = models.Product.objects.all()
    context = {'queryset': queryset}
    return render(request, 'dashboard/product/list.html', context)


def product_detail(request, id):
    queryset = models.Product.objects.get(id=id)
    images = models.ProductImg.objects.filter(product=queryset)
    reviews = models.Review.objects.filter(product=queryset)
    context = {
        'queryset': queryset,
        'images': images,
        'reviews': reviews
    }
    return render(request, 'dashboard/product/detail.html', context)


def product_create(request):
    categorys = models.Category.objects.all()
    context = {'categorys': categorys}
    if request.method == 'POST':
        delivery = True if request.POST.get('delivery') else False
        models.Product.objects.create(
            category_id=request.POST['category_id'],
            name=request.POST['name'],
            body=request.POST['body'],
            price=request.POST['price'],
            banner_img=request.FILES['banner_img'],
            quantity=request.POST['quantity'],
            delivery=delivery
        )
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/product/create.html', context)


def product_update(request, id):
    product = models.Product.objects.get(id=id)
    if request.method == 'POST':
        product.category_id = request.POST['category_id']
        product.name = request.POST['name']
        product.body = request.POST['body']
        product.price = request.POST['price']
        product.banner_img = request.FILES['banner_img']
        product.quantity = request.POST['quantity']
        product.delivery = True if request.POST.get('delivery') else False
        product.save()
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/product/update.html')


def product_delete(request, id):
    product = models.Product.objects.get(id=id)
    product.delete()
    return redirect('dashboard:product_list')
