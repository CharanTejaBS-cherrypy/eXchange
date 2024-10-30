from django.contrib.auth.models import User
from django.db import models


# Product model for Buy and Sell items
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='product_images/', null=True, blank=True)
    contact = models.CharField(max_length=100, help_text="Enter email or phone number",
                               default="+91 1234567890  or user@gmail.com(prefered)")  # New field
    saved_by = models.ManyToManyField(
        User, related_name="saved_products", blank=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name


# User profile to store additional information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    college = models.CharField(max_length=255, null=True, blank=True)
    saved_products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username
