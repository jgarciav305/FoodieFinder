from django.db import models

# Create your models here.

class FoodCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine_type = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    cost_range = models.CharField(max_length=20)  # Example: '$', '$$', '$$$'
    is_open = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    main_photo = models.ImageField(upload_to='restaurant_photos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    favorites = models.ManyToManyField(Restaurant, blank=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super(UserProfile, self).save(*args, **kwargs)

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.restaurant.name}"
