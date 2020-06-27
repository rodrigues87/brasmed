# Generated by Django 3.0.7 on 2020-06-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0007_auto_20200627_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='foto_cpf',
            field=models.FileField(blank=True, null=True, upload_to='uploads/cpf'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='foto_identidade',
            field=models.FileField(blank=True, null=True, upload_to='uploads/identidade'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='proposta_frente',
            field=models.FileField(blank=True, null=True, upload_to='uploads/proposta'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='proposta_verso',
            field=models.FileField(blank=True, null=True, upload_to='uploads/proposta'),
        ),
    ]
