# Generated by Django 3.2.6 on 2021-08-31 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_materiales_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]