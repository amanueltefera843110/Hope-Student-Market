
from .cart import Cart



#creat context processorso our cat can work on all pages 

def cart(request):
	#return the default data from the cart
	return {'cart': Cart(request)}
