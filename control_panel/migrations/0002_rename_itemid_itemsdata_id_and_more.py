# Generated by Django 5.0.4 on 2024-08-16 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemsdata',
            old_name='itemId',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='itemsdata',
            old_name='itemName',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='itemsdata',
            old_name='itemQuantity',
            new_name='Quantity',
        ),
    ]
