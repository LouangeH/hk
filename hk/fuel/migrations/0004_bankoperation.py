# Generated by Django 5.1.7 on 2025-04-23 09:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0003_way_alter_expense_amount_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_operation', models.CharField(choices=[('depot', 'Dépôt'), ('retrait', 'Retrait'), ('tenue', 'Tenue de compte')], max_length=10)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=12)),
                ('motif', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('effectué_par', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Opération bancaire',
                'verbose_name_plural': 'Opérations bancaires',
            },
        ),
    ]
