from django.contrib import admin
from .models import ShipingAddress, Order, OrderItem
from django.contrib.auth.models import User


# Register the model on the admin section thing
admin.site.register(ShipingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

# Create an OrderItem Inline
class OrderItemInline(admin.StackedInline):
	model = OrderItem
	extra = 0# cuz djno want to add

# Extend our Order Model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_order"]  # Makes 'date_order' field read-only
    fields = ["user", "full_name", "email", "shipping_address", "amount_paid", "date_order","shipped","date_shipped"]
    inlines = [OrderItemInline]  # Embeds OrderItemInline within the Order admin panel

# Unregister Order Model
admin.site.unregister(Order)

# Re-Register our Order AND OrderAdmin
admin.site.register(Order, OrderAdmin)