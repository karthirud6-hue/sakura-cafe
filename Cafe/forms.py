from django import forms
from .models import Product


class Product_Form(forms.ModelForm):

    class Meta:
        model = Product

        fields = '__all__'

        widgets = {
            'product_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter product name'
                }
            ),

            'category': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Example: Beverage'
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter price',
                    'step': '0.01'
                }
            ),

            'availability': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),

            'picture': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/*'
                }
            ),
        }