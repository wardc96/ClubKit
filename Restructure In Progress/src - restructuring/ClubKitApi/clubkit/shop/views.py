from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.urls import reverse
from clubkit.clubs.models import ClubInfo
from clubkit.shop.models import Category, Product
from clubkit.shop.forms import CategoryForm, ProductForm
from clubkit.shop.models import Category, Product


class ClubShop(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_shop.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        # user = ClubInfo.objects.filter(user=request.user).first()
        products = Product.objects.filter(club_id=club_pk)
        return Response({'products': products
                         })


class ClubShopCategories(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'categories.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        form = CategoryForm()
        # user = ClubInfo.objects.filter(user=request.user).first()
        category_types = Category.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'category_types': category_types
                         })

    def post(self, request):
        form = CategoryForm(data=request.data)
        user = ClubInfo.objects.filter(user=request.user).first()
        category_types = Category.objects.filter(club_id=user.pk)
        if form.is_valid():
            form.save()
            return redirect('shop:club_shop_categories')
        else:
            return Response({'form': form,
                             'category_types': category_types
                             })


def delete_category(request, pk):
    category_id = Category.objects.filter(pk=pk)
    category_id.delete()
    return redirect('shop:club_shop_categories')


def edit_category(request, pk):
    instance = Category.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('shop:club_shop_categories')
        else:
            return redirect('shop:club_shop_categories')
    else:
        form = CategoryForm(instance=instance)
        return render(request, 'edit_category.html', {'form': form,
                                                      'instance': instance})


class ClubShopProducts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'products.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        form = ProductForm()
        # user = ClubInfo.objects.filter(user=request.user).first()
        products = Product.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'products': products
                         })

    def post(self, request):
        form = ProductForm(data=request.data)
        user = ClubInfo.objects.filter(user=request.user).first()
        products = Product.objects.filter(club_id=user.pk)
        if form.is_valid():
            form.save()
            return redirect('shop:club_shop_products')
        else:
            return Response({'form': form,
                             'products': products
                             })


def delete_product(request, pk):
    product_id = Product.objects.filter(pk=pk)
    product_id.delete()
    return redirect('shop:club_shop_products')


def edit_product(request, pk):
    instance = Product.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('shop:club_shop_products')
        else:
            return redirect('shop:club_shop_products')
    else:
        form = ProductForm(instance=instance)
        return render(request, 'edit_products.html', {'form': form,
                                                      'instance': instance})
'''

class product_detail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product-details.html'

    def get(self, request):

        user = ClubInfo.objects.filter(user=request.user).first()
        products = Product.objects.filter(club_id=user.pk)
        return Response({'products': products
                         })
'''


def product_detail(request, slug):
    products = get_object_or_404(Product, slug=slug, available=True)
    return render(request,'product-details.html',
                {'products': products
                })







'''
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products.html', {'category': category,
                                         'categories': categories,
                                         'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductFrom()
    return render(request,
                  'detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
'''