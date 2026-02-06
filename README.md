# Ex02 Django ORM Web Application
## Date: 05.02.2026

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM

<img width="1536" height="1024" alt="ORM ex1" src="https://github.com/user-attachments/assets/a4c5b402-0601-45c3-88ae-59f770d9b722" />


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

admins.py:
```
from django.contrib import admin
from . models import FoodOrder
admin.site.register(FoodOrder);

# Register your models here.
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'restaurant', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('customer_name', 'restaurant')
```
models.py:
```
from django.db import models

class FoodOrder(models.Model):
    OrderID = models.IntegerField()
    UserID = models.IntegerField(primary_key=True)
    OrderDate = models.DateField()
    ItemName = models.CharField(max_length=100)
    OrderQty = models.IntegerField()
    UnitPrice = models.FloatField(max_length=20)
    TotalAmount = models.FloatField(max_length=20)
    Adress = models.CharField(max_length=100)

    def __str__(self):
        return self.ItemName
```

## OUTPUT


![](OUTPUT.jpg)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
