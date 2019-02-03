from django import forms
from clubkit.shop.models import Category, Product


class ProductForm(forms.ModelForm):

    class Meta():
        model = Product
        fields = ('club_id', 'category', 'name', 'image',
                  'description', 'price', 'size', 'stock',
                  'available')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # self.fields['club_id'].widget = forms.HiddenInput()


class CategoryForm(forms.ModelForm):

    class Meta():
        model = Category
        fields = ('club_id', 'name')

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        # self.fields['club_id'].widget = forms.HiddenInput()
