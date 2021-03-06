# Generated by Django 4.0.4 on 2022-06-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa_Fisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=11)),
                ('RG', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('?', 'Prefiro não informar')], max_length=1)),
                ('data_de_nascimento', models.DateField()),
            ],
        ),
    ]
