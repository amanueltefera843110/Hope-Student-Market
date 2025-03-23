from store.models import Product, Profile

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request

        # Get the current session key if it exists
        cart = self.session.get('session_key', {})

        # If the user is new, initialize cart
        if 'session_key' not in self.session:
            self.session['session_key'] = {}

        self.cart = self.session['session_key']

    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id  in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}  
            self.cart[product_id] = int(product_qty)

        self.session.modified = True  # Mark session as changed

        #check if log in and do somthing
        if  self.request.user.is_authenticated:
            #get person
            curren_user = Profile.objects.filter(user__id=self.request.user.id)
            # change ' '  to "" cuz of Json
            carty = str(self.cart)
            carty = carty.replace("'", '"')
            #save the carty to the modle 
            curren_user.update(old_cart=(carty))
    def db_add(self, product,quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id  in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}  
            self.cart[product_id] = int(product_qty)

        self.session.modified = True  # Mark session as changed

        #check if log in and do somthing
        if  self.request.user.is_authenticated:
            #get person
            curren_user = Profile.objects.filter(user__id=self.request.user.id)
            # change ' '  to "" cuz of Json
            carty = str(self.cart)
            carty = carty.replace("'", '"')
            #save the carty to the modle 
            curren_user.update(old_cart=(carty))






    def __len__(self):
    	return len(self.cart)
    def get_prods(self):
    	# get id
    	product_ids = self.cart.keys()
    	# use id to look for prod
    	product = Product.objects.filter(id__in=product_ids)

    	return product
    def get_quants(self):
        quantities =self.cart
        return quantities
    def update(self, product, quantity):
        product_id = str(product)
        self.cart[product_id] = int(quantity)
        self.session.modified = True
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        if  self.request.user.is_authenticated:
            #get person
            curren_user = Profile.objects.filter(user__id=self.request.user.id)
            # change ' '  to "" cuz of Json
            carty = str(self.cart)
            carty = carty.replace("'", '"')
            #save the carty to the modle 
            curren_user.update(old_cart=(carty))
            
    def cart_total(self):
        #get id
        product_ids = self.cart.keys()
        #look for the keys in the database
        products = Product.objects.filter(id__in=product_ids)
        #get quantity
        quantity = self.cart
        total =0
        for key , value in quantity.items():
            # change key to int to do math
            key= int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total =total+ (product.sale_price * value)
                    else:
                        total =total+ (product.price * value)


        return total






















