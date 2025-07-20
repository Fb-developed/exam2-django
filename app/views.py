from django.shortcuts import render, HttpResponse, redirect
from .models import *

def income_list_view(request):
    if request.method == "GET":
        incomes = Income.objects.all()
        return render(request, "income_list.html", {"income":incomes})
    

def expense_list_view(request):
    if request.method == "GET":
        expenses = Expense.objects.all()
        return render(request, "expense_list.html", {"":expenses})
    
def income_create_view(request):
    if request.method == "GET":
        incomes = Income.objects.all()
        categorys = Category.objects.all()
        return render(request, "income_create.html", {"income":incomes, "category":categorys})
    elif request.method == "POST":
        amount = request.POST.get("amount", False)
        category_id = request.POST.get("category", False)
        description = request.POST.get("description", False)
        user_id = request.POST.get("user_id", False)
        if not amount or not category_id or not description or not user_id:
            return HttpResponse("error")
        category = Category.objects.filter(id=category_id).first()
        user = User.objects.filter(id=user_id).first()
        Income.objects.create(
            amount = amount,
            category = category,
            description= description,
            user = user
        )
    return redirect("income-list")



def expense_create_view(request):
    if request.method == "GET":
        expenses = Expense.objects.all()
        categorys = Category.objects.all()
        return render(request, "income_create.html", {"expense":expenses, "category":categorys})
    elif request.method == "POST":
        amount = request.POST.get("amount", False)
        category_id = request.POST.get("category", False)
        description = request.POST.get("description", False)
        user_id = request.POST.get("user_id")
        if not amount or not category_id or not description:
            return HttpResponse("error")
        category = Category.objects.filter(id=category_id).first()
        user = User.objects.filter(id=user_id).first()
        Expense.objects.create(
            amount = amount,
            category = category,
            description= description,
            user = user
        )
    return redirect("expense-list")
        


def income_edit_view(request, pk):
    incomes = Income.objects.filter(id=pk).first()
    if request.method == "GET":
        return render(request, "income_edit.html", {"income":incomes})
    elif request.method == "POST":
        amount = request.POST.get("amount", False)
        category = request.POST.get("category", False)
        description = request.POST.get("description", False)
        if not amount or not category or not description:
            return HttpResponse("plice fill all inputs")
        incomes.amount = amount,
        incomes.description = description,
        incomes.category = category
        incomes.save()
        return redirect("income_list")
    


def expense_edit_view(request, pk):
    expenses = Expense.objects.filter(id=pk).first()
    if request.method == "GET":
        return render(request, "income_edit.html", {"expenses":expenses})
    elif request.method == "POST":
        amount = request.POST.get("amount", False)
        category = request.POST.get("category", False)
        description = request.POST.get("description", False)
        if not amount or not category or not description:
            return HttpResponse("plice fill all inputs")
        expenses.amount = amount,
        expenses.description = description,
        expenses.category = category
        expenses.save()
        return redirect("expense_list")
    


def income_delete_view(request, pk):
    income = Income.objects.filter(id=pk).first()
    if not income:
        return HttpResponse("Income not found")
    if request.method == "GET":
        return render(request, "confirm_delete_income.html", {"income":income})
    elif request.method == "POST":
        income.delete()
        return redirect("income_list")
    

    
def expense_delete_view(request, pk):
    expenses = Expense.objects.filter(id=pk).first()
    if not expenses:
        return HttpResponse("expenses not found")
    if request.method == "GET":
        return render(request, "confirm_delete_expense.html", {"expense":expenses})
    elif request.method == "POST":
        expenses.delete()
        return redirect("expense_list")
    


def category_create_view(request):
    if request.method == "GET":
        categorys = Category.objects.all()
        print(categorys)
        return render(request, "category_create.html", {"categorys":categorys})
    elif request.method == "POST":
        name = request.POST.get("name", False)
    if not name:
        return HttpResponse("error")
    Category.objects.create(
        name = name
        )
    return redirect("income-list")