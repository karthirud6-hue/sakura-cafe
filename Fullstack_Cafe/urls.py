from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static


def HomePage(request):
    return render(request, 'home.html')


urlpatterns = [

    path('admin/', admin.site.urls),

    path('cafe/', include('Cafe.urls')),

    path('', HomePage, name='home'),

    path('orders/', include('OrderManagement.urls')),

    path('login/', include('authentication.urls')),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)