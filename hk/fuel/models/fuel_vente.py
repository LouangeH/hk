from django.db import models

class FuelSale(models.Model):
    client = models.CharField(max_length=100)
    quantity_liters = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_liter = models.DecimalField(max_digits=10, decimal_places=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=0)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity_liters * self.price_per_liter
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity_liters} L sold to {self.client} on {self.date.date()}"