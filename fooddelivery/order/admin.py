from django.contrib import admin
from . models import FoodOrder
admin.site.register(FoodOrder);

# Register your models here.
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'restaurant', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('customer_name', 'restaurant')