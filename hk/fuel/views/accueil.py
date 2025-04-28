from django.db.models import Sum
from django.shortcuts import render
from fuel.models import FuelPurchase, FuelSale, Expense, Way, BankOperation
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    litre_achats = FuelPurchase.objects.aggregate(Sum('quantity_liters'))['quantity_liters__sum'] or 0
    litre_vendus =  FuelSale.objects.aggregate(Sum('quantity_liters'))['quantity_liters__sum'] or 0
    autres = Way.objects.aggregate(Sum('quantity_liters'))['quantity_liters__sum'] or 0
    vendus =  litre_vendus + autres
    total_achats = FuelPurchase.objects.aggregate(Sum('total_cost'))['total_cost__sum'] or 0
    total_ventes = FuelSale.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0
    autres_revenu = Way.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_vendus = autres_revenu + total_ventes
    total_depenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    benefice = total_vendus - (total_achats + total_depenses)
    stock = litre_achats - vendus

    total_depots = BankOperation.objects.filter(type_operation='depot').aggregate(Sum('montant'))['montant__sum'] or 0
    total_retraits = BankOperation.objects.filter(type_operation='retrait').aggregate(Sum('montant'))['montant__sum'] or 0
    total_tenue = BankOperation.objects.filter(type_operation='tenue').aggregate(Sum('montant'))['montant__sum'] or 0

    solde_banque = total_depots - total_retraits - total_tenue
    solde_caisse = total_vendus - total_depenses - total_depots

    context = {
        'total_achats': total_achats,
        'total_ventes': total_vendus,
        'total_depenses': total_depenses,
        'benefice': benefice,
        'litre_achats':litre_achats,
        'litre_vendus':vendus,
        'stock':stock,
        'total_depots': total_depots,
        'total_retraits': total_retraits,
        'total_tenue': total_tenue,
        'solde_banque': solde_banque,
        'solde_caisse': solde_caisse,
    }
    return render(request, 'fuel/dashboard.html', context)