from django.contrib import admin
from .models import FoodCategory, Restaurant, Review, UserProfile

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(UserProfile)