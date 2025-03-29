from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
import datetime





def create_ShipingAddress(sender, instance, created,**kwargs):
	if created:
		user_ShipingAddress = ShipingAddress(user=instance)
		user_ShipingAddress.save()
post_save.connect(create_ShipingAddress,sender = User)

class ShipingAddress(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
	shipping_full_name = models.CharField(max_length=300, default="")
	shipping_email = models.EmailField(max_length=300, default="example@example.com")
	shipping_address1 = models.CharField(max_length=300)
	shipping_address2 = models.CharField(max_length=300, null=True, blank=True)  # Made nullable # Changed from duplicate address1
	shipping_city = models.CharField(max_length=300)
	shipping_state = models.CharField(max_length=300, null=True, blank=True)
	shipping_zipcode = models.CharField(max_length=300, null=True, blank=True)
	country = models.CharField(max_length=300)

	
	
	# Don't pluralize address
	class Meta:
		verbose_name_plural = "Shipping Address"

	def __str__(self):
		return f'Shipping Address - {str(self.id)}'


class Order(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
	full_name = models.CharField(max_length=300)
	email = models.EmailField(max_length=300)
	shipping_address = models.TextField() 
	amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
	date_order = models.DateTimeField(auto_now_add=True)
	shipped = models.BooleanField(default=False)
	date_shipped = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f'Order -{str(self.id)}'

# Auto Add shipping Date
@receiver(pre_save, sender=Order)
def set_shipped_date_on_update(sender, instance, **kwargs):
	if instance.pk:
		now = datetime.datetime.now()
		obj = sender._default_manager.get(pk=instance.pk)
		if instance.shipped and not obj.shipped:
			instance.date_shipped = now

class OrderItem(models.Model):
	Order = models.ForeignKey(Order, on_delete= models.CASCADE, null=True)
	Product = models.ForeignKey(Product, on_delete= models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)

	quantity = models.PositiveBigIntegerField(default=1)
	price = models.DecimalField(max_digits=7, decimal_places=2 )

	def __str__(self):
		return f'OrderItem _{str(self.id)}'
	










