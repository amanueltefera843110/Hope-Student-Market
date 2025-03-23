from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse 
from django.contrib import messages




# Create your views here.
def cart_summary(request):
    # Get cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants  
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {'cart_products': cart_products, 'quantities': quantities, 'totals':totals})

def cart_add(request):
    # Get cart
    cart = Cart(request)

    # Test for POST request
    if request.POST.get('action') == 'post':
        # Getting the product ID correctly
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # Look up the product
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product,quantity=product_qty)  # Fix method call
        cartnum = cart.__len__()

        # Return a response
        #response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'qty': cartnum })
        messages.success(request, (" Product Added"))
        return response

def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({"product": product_id})
        messages.success(request, ("Item Deleted From Shopping Cart"))
        return response

	
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({"qty": product_qty})
        messages.success(request, ("Your Cart Is Update"))
        return response


