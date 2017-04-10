from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'period', 'price']
    list_editable = ['period', 'price']
    list_filter = ['available', 'created', 'update']
    prepopulated_fields = {'slug':('name', )}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)

