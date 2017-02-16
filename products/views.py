from django.shortcuts import render, redirect
from products.models import Product
from products.helpers import pagination, Pager
from products.forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def products_list(request):
    products = Product.objects.all().order_by('-id')
    print (products)
    page = pagination(request, products, 12)

    return render(request, 'products/index.html', locals())


@login_required
def upload(request):
    form = UploadFileForm()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            p = Product()
            p.description = request.POST['description']
            p.image = request.FILES['file']
            p.user = request.user
            p.price = request.POST['price']
            p.save()

            return redirect('/')

    return render(request, 'products/upload.html', {'form':form})