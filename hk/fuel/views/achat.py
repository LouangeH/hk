from django.shortcuts import render, redirect, get_object_or_404
from fuel.forms import FuelPurchaseForm
from fuel.models import FuelPurchase
from django.contrib.auth.decorators import login_required

@login_required
def fuel_purchase_list(request):
    purchases = FuelPurchase.objects.all()
    return render(request, 'purchases/purchase_list.html', {'purchases': purchases})

@login_required
def create_fuel_purchase(request):
    form = FuelPurchaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fuel_purchase_list')
    return render(request, 'purchases/create_purchase.html', {'form': form})

@login_required
def edit_fuel_purchase(request, pk):
    purchases = get_object_or_404(FuelPurchase, pk=pk)
    form = FuelPurchaseForm(request.POST or None, instance=purchases)
    if form.is_valid():
        form.save()
        return redirect('fuel_purchase_list')
    
    return render(request, 'purchases/create_purchase.html', {'form': form, 'purchases': purchases})

@login_required
def delete_purchase(request, pk):
    purchases = get_object_or_404(FuelPurchase, pk=pk)
    if request.method == 'POST':
        purchases.delete()
        return redirect('fuel_purchase_list')
    return render(request, 'purchases/delete_purchase.html', {'purchases': purchases})


