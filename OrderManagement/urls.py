from django.urls import path
from .views import *

urlpatterns = [

    path('orders/', OrdersListView.as_view()),
    path('add/orders/', OrdersAddView.as_view()),
    path('delete/<int:id>/', OrdersDeleteView.as_view(), name='order_delete'),
    path('update/<int:id>/', OrdersUpdateView.as_view(), name='order_update'),

    path('customers/', CustomerListView.as_view()),
    path('addcustomers/', CustomerAddView.as_view()),
    path('deletecustomers/<int:id>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('updatecustomers/<int:id>/', CustomerUpdateView.as_view(), name='customer_update'),

]