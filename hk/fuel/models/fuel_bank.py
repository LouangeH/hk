from django.db import models
from django.contrib.auth.models import User

class BankOperation(models.Model):
    TYPE_CHOICES = [
        ('depot', 'Dépôt'),
        ('retrait', 'Retrait'),
        ('tenue', 'Tenue de compte'),
    ]

    type_operation = models.CharField(max_length=10, choices=TYPE_CHOICES)
    montant = models.DecimalField(max_digits=12, decimal_places=0)
    motif = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    effectué_par = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.get_type_operation_display()} de {self.montant} FBu le {self.date.date()}"

    class Meta:
        verbose_name = "Opération bancaire"
        verbose_name_plural = "Opérations bancaires"
