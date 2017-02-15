from django.shortcuts import render, redirect
from products.models import Product
from products.helpers import pagination, Pager
from products.forms import UploadFileForm



def products_list(request):
    products = Product.objects.all().order_by('-id')
    print (products)
    page = pagination(request, products, 3)

    return render(request, 'products/index.html', locals())


def upload(request):
    form = UploadFileForm()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            p = Product()
            p.description = request.POST['description']
            p.image = request.FILES['file']
            p.price = request.POST['price']
            p.save()

            return redirect('/')

    return render(request, 'products/upload.html', {'form':form})