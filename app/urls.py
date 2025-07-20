from django.urls import path
from .views import * 


urlpatterns = [
    path("", income_list_view, name="income-list"),
    path("category_create", category_create_view, name="category-create"),
    path("income_create", income_create_view, name="income-create"),
    path("<int:pk>", income_edit_view, name="income-edit"),
    path("delete/<int:pk>", income_delete_view, name="income-delete"),
    path("expense_create", expense_create_view, name="expense-create"),
    path("update/expense/<int:pk>", expense_edit_view, name="expense-edit"),
    path("expense/delete/<int:pk>", expense_delete_view, name="expense-delete")
]
