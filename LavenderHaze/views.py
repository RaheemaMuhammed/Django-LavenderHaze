from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from store.models import Product


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def ghome(request):
    products=Product.objects.all().filter(is_available=True)
    context =   {
        'products':products,
    }
    return render(request,'ghome.html',context)