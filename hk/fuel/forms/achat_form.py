from django import forms
from fuel.models import FuelPurchase

class FuelPurchaseForm(forms.ModelForm):
    class Meta:
        model = FuelPurchase
        fields = ['supplier', 'quantity_liters', 'price_per_liter']