# Generated by Django 4.0.4 on 2022-06-23 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corretores', '0001_initial'),
        ('pagamentos', '0002_remove_pagamento_data_de_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='Corretor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='corretores.corretore'),
            preserve_default=False,
        ),
    ]
