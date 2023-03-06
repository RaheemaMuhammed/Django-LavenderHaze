from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from store.models import Product


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def ghome(request):
    products = Product.objects.order_by('-created_at')[:10]
    context =   {
        'products':products,
    }
    return render(request,'ghome.html',context)