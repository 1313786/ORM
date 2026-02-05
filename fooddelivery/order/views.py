from django.shortcuts import render
from .models import FoodOrder

def order_list(request):
    order = FoodOrder.objects.all()
    return render(request, 'order/order_list.html', {'order': order})