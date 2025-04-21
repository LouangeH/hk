from django.db import models

class Way(models.Model):
    description = models.CharField(max_length=255)
    quantity_liters = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity_liters} - {self.amount}"
    