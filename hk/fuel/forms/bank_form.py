from django import forms
from fuel.models import BankOperation

class BankOperationForm(forms.ModelForm):
    class Meta:
        model = BankOperation
        fields = ['type_operation', 'montant', 'motif']

    def clean(self):
        cleaned_data = super().clean()
        type_operation = cleaned_data.get('type_operation')
        montant = cleaned_data.get('montant')

        if type_operation == 'retrait':
            from fuel.models import BankOperation  # importer ici pour éviter des erreurs circulaires
            from django.db.models import Sum
            
            total_depots = BankOperation.objects.filter(type_operation='depot').aggregate(Sum('montant'))['montant__sum'] or 0
            total_retraits = BankOperation.objects.filter(type_operation='retrait').aggregate(Sum('montant'))['montant__sum'] or 0
            total_tenue = BankOperation.objects.filter(type_operation='tenue').aggregate(Sum('montant'))['montant__sum'] or 0

            solde_disponible = total_depots - total_retraits - total_tenue

            if montant and montant > solde_disponible:
                raise forms.ValidationError(
                    f"Retrait invalide : vous ne pouvez pas retirer plus que {solde_disponible:,.0f} FBu actuellement disponible en banque."
                )

    def clean_type_operation(self):
        type_op = self.cleaned_data['type_operation']
        if type_op == 'tenue':
            raise forms.ValidationError("Vous ne pouvez pas créer une tenue de compte manuellement.")
        return type_op
    
    
