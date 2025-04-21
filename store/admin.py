from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User
from django.contrib.admin.sites import AlreadyRegistered

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)


# Mix user info with profile
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend the user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]

# Unregister old User model and register the extended one
try:
    admin.site.unregister(User)
except AlreadyRegistered:
    pass

admin.site.register(User, UserAdmin)

# Avoid duplicate registration
try:
    admin.site.register(Profile)
except AlreadyRegistered:
    pass
