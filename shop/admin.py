from django.contrib import admin
from .models import Category, Product, Profile

admin.site.register(Profile)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['name', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
