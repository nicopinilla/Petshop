# Generated by Django 3.2.4 on 2021-06-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_categoria_nombrecategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(max_length=80, verbose_name='Nombre de la categoria'),
        ),
    ]