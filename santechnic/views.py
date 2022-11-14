from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views import generic
from .models import Product, Category


class CategoryView(generic.ListView):
    template_name = 'santechnic/home.html'
    context_object_name = 'category_list'
    model = Category
    queryset = Category.objects.filter()


class ProductsView(generic.ListView):
    template_name = 'santechnic/products.html'
    context_object_name = 'products_list'
    model = Product
    queryset = model.objects.all()

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        category = self.kwargs.get('category_name', None)
        return queryset.filter(category=category)

#
# class ProductDetailView(generic.ListView):
#     template_name = 'santechnic/detail.html'
#     model = Product


def about_us(request):
    return render(request, 'santechnic/about_us.html', None)


def contacts(request):
    return render(request, 'santechnic/contacts.html', None)
