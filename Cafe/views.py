from django.shortcuts import render, redirect
from .models import Product
from .forms import Product_Form
from django.views import View


class ProductListView(View):

    def get(self, request):
        context = {
            'all_products': Product.objects.all()
        }

        return render(request, 'products.html', context)


class ProductAddView(View):

    def get(self, request):
        context = {
            'product_form': Product_Form()
        }

        return render(request, 'products_add.html', context)

    def post(self, request):

        product_form = Product_Form(
            request.POST,
            request.FILES
        )

        if product_form.is_valid():
            product_form.save()

            return redirect('/cafe/products/')

        context = {
            'product_form': product_form
        }

        return render(
            request,
            'products_add.html',
            context
        )


class ProductDeleteView(View):

    def get(self, request, id):

        product = Product.objects.get(id=id)

        product.delete()

        return redirect('/cafe/products/')


class ProductUpdateView(View):

    def get(self, request, id):

        product = Product.objects.get(id=id)

        context = {
            'product_form': Product_Form(
                instance=product
            )
        }

        return render(
            request,
            'products_add.html',
            context
        )

    def post(self, request, id):

        product = Product.objects.get(id=id)

        product_form = Product_Form(
            request.POST,
            request.FILES,
            instance=product
        )

        if product_form.is_valid():
            product_form.save()

            return redirect('/cafe/products/')

        context = {
            'product_form': product_form
        }

        return render(
            request,
            'products_add.html',
            context
        )


def HomePage(request):
    return render(request, 'home.html')