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

    def _str_(self):
        return self.ItemName