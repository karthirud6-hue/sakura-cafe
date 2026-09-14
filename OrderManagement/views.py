from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .models import *
from .forms import *


@method_decorator(login_required, name='dispatch')
class OrdersListView(View):

    def get(self, request):
        context = {
            'all_orders': Orders.objects.all()
        }

        return render(request, 'orders.html', context)


@method_decorator(login_required, name='dispatch')
class OrdersAddView(View):

    def get(self, request):
        context = {
            'order_form': Orders_Form()
        }

        return render(request, 'orders_add.html', context)

    def post(self, request):
        order_form = Orders_Form(request.POST)

        if order_form.is_valid():
            order_form.save()
            return redirect('/orders/orders/')


@method_decorator(login_required, name='dispatch')
class OrdersDeleteView(View):

    def get(self, request, id):
        order = Orders.objects.get(id=id)
        order.delete()

        return redirect('/orders/orders/')


@method_decorator(login_required, name='dispatch')
class OrdersUpdateView(View):

    def get(self, request, id):
        order = Orders.objects.get(id=id)

        context = {
            'order_form': Orders_Form(instance=order)
        }

        return render(request, 'orders_add.html', context)

    def post(self, request, id):
        order = Orders.objects.get(id=id)

        order_form = Orders_Form(
            request.POST,
            instance=order
        )

        if order_form.is_valid():
            order_form.save()
            return redirect('/orders/orders/')


@method_decorator(login_required, name='dispatch')
class CustomerListView(View):

    def get(self, request):
        context = {
            'all_customers': Customer.objects.all()
        }

        return render(request, 'customers.html', context)


@method_decorator(login_required, name='dispatch')
class CustomerAddView(View):

    def get(self, request):
        context = {
            'customer_form': Customer_Form()
        }

        return render(request, 'customers_add.html', context)

    def post(self, request):
        customer_form = Customer_Form(request.POST)

        if customer_form.is_valid():
            customer_form.save()
            return redirect('/orders/customers/')


@method_decorator(login_required, name='dispatch')
class CustomerDeleteView(View):

    def get(self, request, id):
        customer = Customer.objects.get(id=id)
        customer.delete()

        return redirect('/orders/customers/')


@method_decorator(login_required, name='dispatch')
class CustomerUpdateView(View):

    def get(self, request, id):
        customer = Customer.objects.get(id=id)

        context = {
            'customer_form': Customer_Form(instance=customer)
        }

        return render(request, 'customers_add.html', context)

    def post(self, request, id):
        customer = Customer.objects.get(id=id)

        customer_form = Customer_Form(
            request.POST,
            instance=customer
        )

        if customer_form.is_valid():
            customer_form.save()
            return redirect('/orders/customers/')