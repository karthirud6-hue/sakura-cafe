from django import forms

from .models import Customer, Orders


class Customer_Form(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'customer_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'customer_since': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }


class Orders_Form(forms.ModelForm):

    class Meta:
        model = Orders

        fields = [
            'customer_reference',
            'product_reference',
            'order_number',
            'order_date',
            'quantity'
        ]

        widgets = {
            'customer_reference': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'product_reference': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'order_number': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'order_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
        }