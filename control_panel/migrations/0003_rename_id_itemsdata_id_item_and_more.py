# Generated by Django 5.0.4 on 2024-08-16 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0002_rename_itemid_itemsdata_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemsdata',
            old_name='Id',
            new_name='id_item',
        ),
        migrations.RenameField(
            model_name='itemsdata',
            old_name='Name',
            new_name='name_item',
        ),
        migrations.RenameField(
            model_name='itemsdata',
            old_name='Quantity',
            new_name='quantity_item',
        ),
    ]
