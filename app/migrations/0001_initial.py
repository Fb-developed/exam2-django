# Generated by Django 5.2.4 on 2025-07-20 12:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
                'db_table': 'expense',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_category', to='app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Incomes',
                'db_table': 'income',
                'managed': True,
            },
        ),
    ]
