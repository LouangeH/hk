from django.shortcuts import render, redirect, get_object_or_404
from fuel.forms import WayForm
from fuel.models import Way
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def create_way(request):
    form = WayForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('way_list')
    return render(request, 'ways/create_sale.html', {'form': form})

@login_required
def list_way(request):
    sales = Way.objects.all().order_by('-date')
    paginator = Paginator(sales, 10)  # 10 achats par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ways/sale_list.html', {'page_obj': page_obj,'sales': sales})

@login_required
def edit_way(request, pk):
    sales = get_object_or_404(Way, pk=pk)
    form = WayForm(request.POST or None, instance=sales)
    if form.is_valid():
        form.save()
        return redirect('way_list')
    
    return render(request, 'ways/create_sale.html', {'form': form, 'sales': sales})

@login_required
def delete_way(request, pk):
    sales = get_object_or_404(Way, pk=pk)
    if request.method == 'POST':
        sales.delete()
        return redirect('way_list')
    return render(request, 'ways/delete_sale.html', {'sales': sales})
