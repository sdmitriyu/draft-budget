from django.shortcuts import render, redirect
from .models import Income, Expense

def index(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    remaining = total_income - total_expense

    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'remaining': remaining,
    }
    return render(request, 'index.html', context)

def add_income(request):
    if request.method == 'POST':
        amount = request.POST.get('incomeAmount')
        if amount:
            Income.objects.create(amount=amount)
        return redirect('index')

def add_expense(request):
    if request.method == 'POST':
        date = request.POST.get('expenseDate')
        amount = request.POST.get('expenseAmount')
        description = request.POST.get('expenseDescription')
        if date and amount and description:
            Expense.objects.create(date=date, amount=amount, description=description)
        return redirect('index')