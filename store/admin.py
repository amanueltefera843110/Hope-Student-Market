from django.contrib import admin
from. models import Category,Customer, Product, Order,Profile
from django.contrib.auth.models import User


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
# Register your models here.

#mix user info with profile

class ProfileInline(admin.StackedInline):
	model = Profile
#extand the user to have the new thing

class UserAdmin(admin.ModelAdmin):
	model=User
	field =['username', 'first_name', 'last_name', 'email']
	inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)
# new way
admin.site.register(User,UserAdmin)


