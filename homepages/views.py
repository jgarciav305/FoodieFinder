from django.shortcuts import render
from foodsites.models import UserProfile, Restaurant
from django.shortcuts import render, get_object_or_404
# Create your views here.
def indexPageView(request):
    return render(request, 'homepages/index.html')

def aboutPageView(request):
    return render(request, 'homepages/about.html')

def showCustomersPageView(request):
    data = UserProfile.objects.all()
    context = {
        "cust": data
    }
    return render(request, 'homepages/showCustomers.html', context)

def showSingleCustomerPageView(request, cust_id):
    data = UserProfile.objects.get(id=cust_id)
    favorites = data.favorites.all()
    context = {
        "record": data,
        "favorites":favorites
    }
    return render(request, 'homepages/editCustomer.html', context)

def updateCustomersPageView(request):
    if request.method == 'POST':
        cust_id = request.POST['cust_id']
        customer = UserProfile.objects.get(id=cust_id)

        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.username = request.POST['username']
        customer.email = request.POST['email']
        
        customer.save()

        return showCustomersPageView(request)
    
def deleteCustomerPageView(request, cust_id):
    customer = UserProfile.objects.get(id=cust_id)
    customer.delete()
    return showCustomersPageView(request)

def addCustomerPageView(request):
    if request.method == 'POST':
        customer = UserProfile()
        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.username = request.POST['user_name']
        customer.email = request.POST['email']
        customer.save()
        return showCustomersPageView(request)
    else:
        return render(request, 'homepages/addCustomer.html') 

def addFavoriteRestaurantPageView(request, cust_id):
    data = get_object_or_404(UserProfile, id=cust_id)
    favorites = data.favorites.all()
    avail_restaurants = Restaurant.objects.exclude(id__in=favorites)

    if request.method == "POST":
        restaurant_id = request.POST.get("restaurant")
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        data.favorites.add(restaurant)
        return showCustomersPageView(request)

    context = {
        "customer": data,
        "favorites": favorites,
        "avail_restaurants": avail_restaurants
    }
    return render(request, 'homepages/addFavorite.html', context)

