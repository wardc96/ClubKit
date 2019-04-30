from decimal import Decimal
from django.conf import settings
from clubkit.shop.models import Product
from clubkit.clubs.models import Packages


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


class CartPackage(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_PACKAGE_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_PACKAGE_SESSION_ID] = {}
        self.cart = cart

    def add(self, package):
        package_id = str(package.id)
        if package_id not in self.cart:
            self.cart[package_id] = {'price': str(package.price)}
        self.save()

    def save(self):
        self.session[settings.CART_PACKAGE_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, package):
        package_id = str(package.id)
        if package_id in self.cart:
            del self.cart[package_id]
            self.save()

    def __iter__(self):
        package_ids = self.cart.keys()
        packages = Packages.objects.filter(id__in=package_ids)
        for package in packages:
            self.cart[str(package.id)]['package'] = package

        for item in self.cart.values():
            item['price'] = (item['price'])
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_PACKAGE_SESSION_ID]
        self.session.modified = True

