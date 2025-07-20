from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
     user = models.ForeignKey(User, related_name="income_user", on_delete=models.CASCADE)
     amount = models.FloatField()
     category = models.ForeignKey("Category", related_name="income_category", on_delete=models.CASCADE)
     description = models.TextField(null=True, blank=True)
     created_at = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.category
     
     class Meta:
        db_table = 'income'
        managed = True
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'


class Expense(models.Model):
    user = models.ForeignKey(User, related_name="expense_user", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category
    

    class Meta:
        db_table = 'expense'
        managed = True
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
