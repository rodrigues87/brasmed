# Generated by Django 3.0.7 on 2020-06-27 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0006_solicitacao_comprovante_verso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitacao',
            old_name='comprovante',
            new_name='proposta_frente',
        ),
        migrations.RenameField(
            model_name='solicitacao',
            old_name='comprovante_verso',
            new_name='proposta_verso',
        ),
    ]
