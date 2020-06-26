# Generated by Django 3.0.7 on 2020-06-26 23:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=150)),
                ('identidade', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Apenas números são permitidos')])),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Apenas números são permitidos')])),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('modalidade_de_pagamento', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito')], max_length=1)),
                ('numero_do_cartao', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Apenas números são permitidos')])),
                ('nome_no_cartao', models.CharField(max_length=30)),
                ('validade', models.DateField()),
                ('codigo_de_seguranca', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Apenas números são permitidos')])),
                ('comprovante', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Solicitações',
            },
        ),
    ]