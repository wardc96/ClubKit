from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.urls import reverse
from clubkit.clubs.models import ClubInfo
from clubkit.shop.models import Category, Product
from clubkit.shop.forms import CategoryForm, ProductForm
from clubkit.shop.models import Category, Product
from clubkit.cart.forms import CartAddProductForm

'''
class ClubShop(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_shop.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        # user = ClubInfo.objects.filter(user=request.user).first()
        # products = Product.objects.filter(club_id=club_pk)
        return Response({
            #'products': products,
                         'club_pk': club_pk
                         })
'''


def product_list(request, category_slug=None):
    hidecart = False
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    category = None
    categories = Category.objects.filter(club_id=club_pk)
    products = Product.objects.filter(available=True, club_id=club_pk)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'club_pk': club_pk,
        'club': club,
        'hidecart': hidecart
    }
    return render(request, 'list.html', context)


def product_detail(request, id, slug):
    hidecart = False
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'club_pk': club_pk,
        'club': club,
        'hidecart': hidecart
    }
    return render(request, 'detail.html', context)


class ClubShopCategories(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'categories.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        club_info = ClubInfo.objects.filter(user=request.user).first()
        inital_data = {
            'club_id': club_info,
        }
        form = CategoryForm(initial=inital_data)
        # user = ClubInfo.objects.filter(user=request.user).first()
        category_types = Category.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'category_types': category_types,
                         'club_pk': club_pk,
                         'club': club
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
                             'category_types': category_types,
                             })


def delete_category(request, pk):
    category_id = Category.objects.filter(pk=pk)
    category_id.delete()
    return redirect('shop:club_shop_categories')


def edit_category(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
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
                                                      'instance': instance,
                                                      'club': club
                                                      })


class ClubShopProducts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'products.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        club_info = ClubInfo.objects.filter(user=request.user).first()
        inital_data = {
            'club_id': club_info,
        }
        form = ProductForm(initial=inital_data)
        form.fields['category'].queryset = Category.objects.filter(club_id=club_pk)
        # user = ClubInfo.objects.filter(user=request.user).first()
        products = Product.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'products': products,
                         'club_pk': club_pk,
                         'club': club
                         })

    def post(self, request):
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
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
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    instance = Product.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('shop:club_shop_products')
        else:
            return redirect('shop:club_shop_products')
    else:
        form = ProductForm(instance=instance)
        form.fields['category'].queryset = Category.objects.filter(club_id=club_pk)
        return render(request, 'edit_products.html', {'form': form,
                                                      'instance': instance,
                                                      'club': club
                                                      })


def edit_category(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
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
                                                      'instance': instance,
                                                      'club': club
                                                      })

'''
def add_product(request):
    form = ProductForm(data=request.data)
    user = ClubInfo.objects.filter(user=request.user).first()
    products = Product.objects.filter(club_id=user.pk)
    if form.is_valid():
        form.save()
        return redirect('shop:add_product')
    else:
        return render(request, 'products.html', {'form': form,
                                                 'products': products})
'''

