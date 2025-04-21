from django.db.models import Sum
from django.shortcuts import render
from fuel.models import FuelPurchase, FuelSale, Expense, Way
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

    context = {
        'total_achats': total_achats,
        'total_ventes': total_vendus,
        'total_depenses': total_depenses,
        'benefice': benefice,
        'litre_achats':litre_achats,
        'litre_vendus':vendus,
        'stock':stock,
    }
    return render(request, 'fuel/dashboard.html', context)