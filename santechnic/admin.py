from django.contrib import admin, redirects
from .models import Category, Product

# class CategoryAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['category_name']}),
#         (None, {'fields': ['category_image']}),
#     ]
#
#
# class ProductAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['category']}),
#         (None, {'fields': ['product_name']}),
#         (None, {'fields': ['length']}),
#         (None, {'fields': ['width']}),
#         (None, {'fields': ['height']}),
#         (None, {'fields': ['product_image']}),
#     ]


admin.site.register(Category)
admin.site.register(Product)
#admin.site(Redirects)
