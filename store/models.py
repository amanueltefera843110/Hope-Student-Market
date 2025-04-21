from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save#saveer




#make prof one to one and also can delet
class Profile (models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	datetime_mod = models.DateTimeField(User , auto_now=True)
	phone = models.CharField(max_length=30, blank=True)
	address1 =models.CharField(max_length=300, blank=True)
	address1 =models.CharField(max_length=300, blank=True)
	city = models.CharField(max_length=300, blank=True)
	state = models.CharField(max_length=300, blank=True)
	zipcode=models.CharField(max_length=300, blank=True)
	country = models.CharField(max_length=300, blank=True)
	old_cart= models.CharField(max_length=300, blank=True, null=True)
	def __str__(self):
		return self.user.username

		

# when regiester make pfp
def create_profile(sender, instance, created,**kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
post_save.connect(create_profile,sender = User)


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Customer(models.Model):
	firs_name = models.CharField(max_length=50)
	last_name =models.CharField(max_length=50)
	phone=models.CharField(max_length=10)
	email= models.EmailField(max_length=100)
	password= models.CharField(max_length=100)


	def __str__(self):
		return f'{self.first_name} {self.lastname}'
		

#all of the proudects
class Product(models.Model):
    youStudentID = models.CharField(
        max_length=100,
        default="",      
        blank=False       
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', blank=False, null=False)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name

#custmer orders 
class Order(models.Model):
	product= models.ForeignKey(Product, on_delete= models.CASCADE)
	customer= models.ForeignKey(Customer, on_delete= models.CASCADE )
	quantity= models.IntegerField(default=1)
	address =  models.CharField(max_length=100, default='', blank= True)
	phone= models.CharField(max_length= 20, default= '', blank=True)
	date= models.DateField( default = datetime.datetime.today)
	status= models.BooleanField(default=False)

	def __str__(self):
		return self.product



# Create your models here.
