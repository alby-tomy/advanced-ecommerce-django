from django.contrib import admin
from .models import Category, Product

# Register your models here.
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','original_price','selling_price']
    list_editable = ['original_price','selling_price']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 15
    
admin.site.register(Product, ProductAdmin)