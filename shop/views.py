from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    categories = Category.objects.all()
    things = Thing.objects.all()
    return render(request, 'shop/index.html', context={'categories': categories, 'things': things})


def things_list_all(request):
    things = Thing.objects.all()
    return render(request, 'shop/things_list.html', context={'things': things})


def thing_detail(request, thing_id):
    thing = Thing.objects.get(pk=thing_id)
    return render(request, 'shop/things_detail.html', context={'thing': thing})


def things_list_category(request, thing_category):
    things = Thing.objects.filter(category__category_name=thing_category)
    return render(request, 'shop/things_list.html', context={'things': things})


def things_list_brand(request, thing_brand):
    things = Thing.objects.filter(brand=thing_brand)
    return render(request, 'shop/things_list.html', context={'things': things})




