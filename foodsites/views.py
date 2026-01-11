from django.shortcuts import render
from .models import FoodCategory, Restaurant

# Create your views here.
def showfoodPageView(request):
    return render(request, 'foodsites/showFood.html')

def newyorkPageView(request):
    restaurant= Restaurant.objects.get(city = "New York City")
    context = {
        "city" : restaurant.city,
        "image" : restaurant.main_photo
    }
    return render(request, 'foodsites/displayfood.html', context)

def chicagoPageView(request):
    restaurant= Restaurant.objects.get(city = "Chicago")
    context = {
        "city" : restaurant.city,
        "image" : restaurant.main_photo
    }
    return render(request, 'foodsites/displayfood.html', context)

def langelesPageView(request):
    restaurant= Restaurant.objects.get(city = "Los Angeles")
    context = {
        "city" : restaurant.city,
        "image" : restaurant.main_photo
    }
    return render(request, 'foodsites/displayfood.html', context)

def austinPageView(request):
    restaurant= Restaurant.objects.get(city = "Austin")
    context = {
        "city" : restaurant.city,
        "image" : restaurant.main_photo
    }
    return render(request, 'foodsites/displayfood.html', context)

def norleansPageView(request):
    restaurant= Restaurant.objects.get(city = "New Orleans")
    context = {
        "city" : restaurant.city,
        "image" : restaurant.main_photo
    }
    return render(request, 'foodsites/displayfood.html', context)

def sfriscoPageView(request):
    restaurant= Restaurant.objects.get(city = "San Francisco")
    context = {
        "city" : restaurant.city,
        "image" : restaurant.main_photo
    }
    return render(request, 'foodsites/displayfood.html', context)