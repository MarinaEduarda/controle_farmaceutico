# Generated by Django 5.0.7 on 2024-08-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_animal_options_alter_autorizado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='quantidade',
            field=models.IntegerField(default=0, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='autorizado',
            name='senha',
            field=models.CharField(default='ifsuldeminas', max_length=100, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='lote',
            field=models.CharField(max_length=100, verbose_name='Lote'),
        ),
    ]
