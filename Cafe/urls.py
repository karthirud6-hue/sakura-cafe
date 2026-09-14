from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/add/', ProductAddView.as_view()),
    path('products/delete/<int:id>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/update/<int:id>/', ProductUpdateView.as_view(), name='product_update'),
]