from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from fuel.models import BankOperation
from fuel.forms import BankOperationForm
from django.core.paginator import Paginator

@login_required
def bank_operation_list(request):
    operations = BankOperation.objects.order_by('-date')
    paginator = Paginator(operations, 10)  # 10 achats par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bank/operation_list.html', {'operations': operations, 'page_obj': page_obj})


@login_required
def create_bank_operation(request):
    form = BankOperationForm(request.POST or None)
    if form.is_valid():
        operation = form.save(commit=False)
        operation.effectué_par = request.user
        operation.save()
        return redirect('bankoperation_list')
    return render(request, 'bank/create_operation.html', {'form': form})


@login_required
def update_bank_operation(request, pk):
    operation = get_object_or_404(BankOperation, pk=pk)
    if operation.type_operation == 'tenue':
        return redirect('bankoperation_list')  # Interdit
    form = BankOperationForm(request.POST or None, instance=operation)
    if form.is_valid():
        form.save()
        return redirect('bankoperation_list')
    return render(request, 'bank/create_operation.html', {'form': form})


@login_required
def delete_bank_operation(request, pk):
    operation = get_object_or_404(BankOperation, pk=pk)
    if operation.type_operation == 'tenue':
        return redirect('bankoperation_list')  # Interdit
    if request.method == "POST":
        operation.delete()
        return redirect('bankoperation_list')
    return render(request, 'bank/confirm_delete.html', {'operation': operation})
