from django.shortcuts import render, redirect, get_object_or_404
from fuel.forms import FuelSaleForm
from fuel.models import FuelSale
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def create_fuel_sale(request):
    form = FuelSaleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fuel_sale_list')
    return render(request, 'sales/create_sale.html', {'form': form})

@login_required
def fuel_sale_list(request):
    sales = FuelSale.objects.all().order_by('-date')
    paginator = Paginator(sales, 10)  # 10 achats par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sales/sale_list.html', {'sales': sales, 'page_obj': page_obj})

@login_required
def edit_fuel_sale(request, pk):
    sales = get_object_or_404(FuelSale, pk=pk)
    form = FuelSaleForm(request.POST or None, instance=sales)
    if form.is_valid():
        form.save()
        return redirect('fuel_sale_list')
    
    return render(request, 'sales/create_sale.html', {'form': form, 'sales': sales})

@login_required
def delete_sale(request, pk):
    sales = get_object_or_404(FuelSale, pk=pk)
    if request.method == 'POST':
        sales.delete()
        return redirect('fuel_sale_list')
    return render(request, 'sales/delete_sale.html', {'sales': sales})
