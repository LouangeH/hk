from django import forms
from fuel.models import FuelSale, FuelPurchase, Way
from django.db.models import Sum

class FuelSaleForm(forms.ModelForm):
    class Meta:
        model = FuelSale
        fields = ['client', 'quantity_liters', 'price_per_liter']

    def clean_quantity_liters(self):
            quantity = self.cleaned_data.get('quantity_liters')

            # Calcul du stock
            total_achats = FuelPurchase.objects.aggregate(Sum('quantity_liters'))['quantity_liters__sum'] or 0
            total_ventes = FuelSale.objects.aggregate(Sum('quantity_liters'))['quantity_liters__sum'] or 0
            total_ways = Way.objects.aggregate(Sum('quantity_liters'))['quantity_liters__sum'] or 0
            stock_disponible = total_achats - (total_ventes + total_ways)

            if quantity > stock_disponible:
                raise forms.ValidationError(
                    f"Stock insuffisant : vous disposez de seulement {stock_disponible} L en stock."
                )
            return quantity