from django.shortcuts import render, redirect, get_object_or_404
from fuel.forms import ExpenseForm
from fuel.models import Expense
from django.contrib.auth.decorators import login_required

@login_required
def create_expense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('expense_list')
    return render(request, 'expenses/create_expense.html', {'form': form})

@login_required
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

@login_required
def edit_expense(request, pk):
    expenses = get_object_or_404(Expense, pk=pk)
    form = ExpenseForm(request.POST or None, instance=expenses)
    if form.is_valid():
        form.save()
        return redirect('fuel_sale_list')
    
    return render(request, 'expenses/create_expense.html', {'form': form, 'expenses': expenses})

@login_required
def delete_expense(request, pk):
    expenses = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expenses.delete()
        return redirect('fuel_sale_list')
    return render(request, 'expenses/delete_expense.html', {'expenses': expenses})
